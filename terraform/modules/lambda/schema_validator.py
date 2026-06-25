import csv
import json
import os
import urllib.parse
import boto3

s3 = boto3.client("s3")
sns = boto3.client("sns")

REQUIRED_COLUMNS = {
    "subscribers": ["customer_id", "name", "plan"]
}


def lambda_handler(event, context):
    print("Received event:", json.dumps(event))

    detail = event.get("detail", {})
    bucket = detail.get("bucket", {}).get("name")
    key = detail.get("object", {}).get("key")

    if not bucket or not key:
        raise ValueError("Missing bucket or object key in event")

    key = urllib.parse.unquote_plus(key)

    if not key.startswith("landing/"):
        print(f"Ignoring non-landing object: {key}")
        return {
            "statusCode": 200,
            "body": json.dumps("Ignored non-landing object")
        }

    print(f"Validating file: s3://{bucket}/{key}")

    try:
        if not key.endswith((".csv", ".json", ".parquet")):
            raise ValueError(f"Unsupported file type: {key}")

        if key.endswith(".csv"):
            dataset_name = key.split("/")[-1].replace(".csv", "")
            validate_csv_schema(bucket, key, dataset_name)

        raw_key = key.replace("landing/", "raw/", 1)
        move_file(bucket, key, raw_key)

        print(f"Schema validation passed for {key}")
        print(f"File moved to s3://{bucket}/{raw_key}")

        return {
            "statusCode": 200,
            "body": json.dumps("Schema validation passed")
        }

    except Exception as e:
        error_message = str(e)
        print(f"Schema validation failed: {error_message}")

        quarantine_key = key.replace("landing/", "quarantine/", 1)

        try:
            move_file(bucket, key, quarantine_key)
            print(f"File moved to quarantine: s3://{bucket}/{quarantine_key}")
        except Exception as move_error:
            print(f"Could not move file to quarantine: {move_error}")

        sns.publish(
            TopicArn=os.environ["SNS_TOPIC_ARN"],
            Subject="CVM Schema Validation Failed",
            Message=f"""
Schema validation failed.

Bucket: {bucket}
Source file: {key}
Quarantine file: {quarantine_key}

Reason:
{error_message}
"""
        )

        raise


def validate_csv_schema(bucket, key, dataset_name):
    if dataset_name not in REQUIRED_COLUMNS:
        raise ValueError(f"No schema defined for dataset: {dataset_name}")

    response = s3.get_object(Bucket=bucket, Key=key)
    content = response["Body"].read().decode("utf-8").splitlines()

    reader = csv.DictReader(content)
    actual_columns = reader.fieldnames or []

    missing_columns = [
        column for column in REQUIRED_COLUMNS[dataset_name]
        if column not in actual_columns
    ]

    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    print(f"CSV schema validation passed for {key}")


def move_file(bucket, source_key, destination_key):
    s3.copy_object(
        Bucket=bucket,
        CopySource={"Bucket": bucket, "Key": source_key},
        Key=destination_key
    )

    s3.delete_object(
        Bucket=bucket,
        Key=source_key
    )
