import json
import os
import boto3
from botocore.exceptions import ClientError

glue = boto3.client("glue")


def lambda_handler(event, context):
    print("Received event:", json.dumps(event))

    crawler_name = os.environ["CRAWLER_NAME"]

    try:
        response = glue.start_crawler(Name=crawler_name)
        print(f"Started crawler: {crawler_name}")
        print("Response:", response)

        message = "Crawler started"

    except ClientError as e:
        error_code = e.response["Error"]["Code"]

        if error_code == "CrawlerRunningException":
            print(f"Crawler already running: {crawler_name}")
            message = "Crawler already running"
        else:
            print(f"Failed to start crawler: {error_code}")
            raise

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": message,
            "crawler_name": crawler_name
        })
    }
