import json
import boto3
import pandas as pd
import os

AWS_S3_BUCKET = os.getenv("S3_BUCKET")
def lambda_handler(event, context):
    s3_client = boto3.client("s3")

    response = s3_client.get_object(Bucket=AWS_S3_BUCKET, Key="data_all_mountains.csv")

    status = response.get("ResponseMetadata", {}).get("HTTPStatusCode")

    if status == 200:
        print(f"Successful S3 get_object response. Status - {status}")
        mountains_df = pd.read_csv(response.get("Body"))
    else:
        print(f"Unsuccessful S3 get_object response. Status - {status}")

    print(mountains_df)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
