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
    number_of_days = len(date_range)

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

        single_mountain_data = mountains_df[mountains_df['mountain_name'] == best_single_mountain]

        json_data = {}
        json_data['mountain_name'] = best_single_mountain
        json_data['url'] = single_mountain_data['url'].unique()[0]

        weather_list = []

        day_of_the_week = single_mountain_data['day_of_the_week'].tolist()
        day_of_the_month = single_mountain_data['day_of_the_month'].tolist()
        time_list = single_mountain_data['time'].tolist()
        weather_description = single_mountain_data['weather_description'].tolist()
        weather_icon_urls = single_mountain_data['weather_icon_urls'].tolist()
        wind = single_mountain_data['wind'].tolist()

        for i in range(0, number_of_days):
            day_data = {}
            day_data["date"] = day_of_the_month[i*3]
            day_data["day_of_week"] = day_of_the_week[i*3]
            time_data = []
            for j in range(0, 3):
                weather_instance = {}
                weather_instance['time'] = time_list[i + j]
                weather_instance['weather_description'] = weather_description[i + j]
                weather_instance['wind'] = wind[i + j]
                weather_instance['weather_icon'] = weather_icon_urls[i + j]
                time_data.append(weather_instance)

            day_data['detailed_weather'] = time_data
            weather_list.append(day_data)

        json_data['weather'] = weather_list

        return {
            'statusCode': 200,
            'body': json.dumps(json_data)
        }

    else:
        print(f"Unsuccessful S3 get_object response. Status - {status}")


    return {
        'statusCode': 500,
        'body': json.dumps('Hello from Lambda!')
    }
