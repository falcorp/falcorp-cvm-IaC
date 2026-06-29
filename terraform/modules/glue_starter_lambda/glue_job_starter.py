import json
import os
import boto3

glue = boto3.client("glue")


def lambda_handler(event, context):
    print("Received event:", json.dumps(event))

    job_name = os.environ["GLUE_JOB_NAME"]

    response = glue.start_job_run(JobName=job_name)

    print(f"Started Glue job: {job_name}")
    print(f"JobRunId: {response['JobRunId']}")

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Glue job started",
            "job_name": job_name,
            "job_run_id": response["JobRunId"]
        })
    }
