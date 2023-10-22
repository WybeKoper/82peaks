import json
import boto3
import pandas
import pandas as pd
import os

AWS_S3_BUCKET = os.getenv("S3_BUCKET")
def lambda_handler(event, context):
    s3_client = boto3.client("s3")
    AWS_S3_BUCKET = "peaks-bucket-mainly-wanted-swan"
    response = s3_client.get_object(Bucket=AWS_S3_BUCKET, Key="data_all_mountains.csv")

    start_date = "25-10-2023"
    end_date = "27-10-2023"

    date_range = list(pandas.date_range(start_date, end_date, freq='d'))
    date_of_the_month_set = set()
    for date in date_range:
        date_of_the_month_set.add(date.day)

    status = response.get("ResponseMetadata", {}).get("HTTPStatusCode")

    if status == 200:
        print(f"Successful S3 get_object response. Status - {status}")
        mountains_df = pd.read_csv(response.get("Body"))
        mountains_df = mountains_df[mountains_df['day_of_the_month'].isin(date_of_the_month_set)]

        grouped_mountains = mountains_df.groupby(['mountain_name'], as_index=False).sum()
        best_mountains = grouped_mountains[grouped_mountains.weather_points == grouped_mountains.weather_points.min()]
        best_single_mountain = list(best_mountains['mountain_name'])[0]
        print(best_single_mountain)

    else:
        print(f"Unsuccessful S3 get_object response. Status - {status}")


    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

lambda_handler("test", "test")