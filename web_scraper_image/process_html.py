import json
import pandas as pd
from bs4 import BeautifulSoup
import boto3
from io import StringIO
import re
import os

dir_path = "scrape_responses"


def process_html_responses():
    data_all_mountains = pd.DataFrame()

    print("started processing")
    for file_path in os.listdir(dir_path):
        mountain_name = file_path.replace(".json", "")

        with open(dir_path + "/" + file_path, encoding="utf8") as jsonFile:
            data = json.load(jsonFile)
            elevations_list = list(data['elevations'].keys())
            elevations_list = [int(x) for x in elevations_list]
            highest_elevation = max(elevations_list)
            soup = BeautifulSoup(data['elevations'][str(highest_elevation)]['period_types']['p']['table'],
                                 'html.parser')

            mountain_url = f"https://mountain-forecast.com/peaks/{mountain_name}/forecasts/{highest_elevation}"

            dates = []
            # extract dates from the dates table
            for day in soup.find_all(class_='forecast__table-days-content'):
                text = day.get_text()
                text_no_spaces = text.strip()
                text_no_line_breaks = text_no_spaces.replace("\n", "")
                text_single_spaces = " ".join(text_no_line_breaks.split())
                dates.append(text_single_spaces)

            # get times
            start_index = 0
            times, day_of_the_month, day_of_the_week, = [], [], []
            for time in soup.find_all(class_="forecast__table-time"):
                text = time.get_text()
                text_no_spaces = text.strip()
                text_no_line_breaks = text_no_spaces.replace("\n", "")
                text_single_spaces = " ".join(text_no_line_breaks.split())
                text_list = text_single_spaces.split(" ")
                for val in text_list:
                    if val not in {"night", "AM", "PM"}:
                        continue
                    split_date = dates[start_index].split(" ")
                    day_of_the_week.append(split_date[0])
                    day_of_the_month.append(split_date[1])
                    times.append(val)
                    if val == "night":
                        start_index += 1

            # get weather description text
            weather = []
            for weather in soup.find_all(class_="forecast__table-summary"):
                text = weather.get_text()
                text_no_spaces = text.strip()
                text_no_line_breaks = text_no_spaces.split("\n")
                formated_text = [x.strip() for x in text_no_line_breaks]
                final_text = [x for x in formated_text if x.strip() != ""]
                weather = final_text

            # get icons
            weather_icon_urls = []
            for weather_icon in soup.find_all(class_="forecast__table-weather"):
                image = weather_icon.find_all('img')
                weather_icon_urls = ["https://www.mountain-forecast.com" + url['src'] for url in image]

            # get wind value
            wind = []
            for val in soup.find_all(class_="forecast__table-wind-container"):
                text = val.get_text()
                text_no_spaces = text.strip()
                wind.append(text_no_spaces)

            # calculate weather points for a particular day
            point_map = {"clear": 0, "some clouds": 15, "cloudy": 30, "light snow": 30, "mod. snow": 60,
                         "snow shwrs": 90, "heavy snow": 120, "light rain": 30, "mod. rain": 60, "rain shwrs": 90,
                         "heavy rain": 120, "risk tstorm": 120}
            points = []
            for i in range(0, len(weather)):
                wind_number = int(re.sub('\D', '', wind[i]))
                if weather[i] in point_map:
                    points.append(wind_number + point_map[weather[i]])
                else:
                    points.append(wind_number + 50)

            # construct dataframe
            df = pd.DataFrame({"mountain_name": mountain_name, "day_of_the_week": day_of_the_week,
                               "day_of_the_month": day_of_the_month, "time": times, "weather_description": weather,
                               "weather_icon_urls": weather_icon_urls, "wind": wind, "url": mountain_url,
                               "weather_points": points})

            data_all_mountains = pd.concat([data_all_mountains, df], ignore_index=True)

    data_all_mountains.to_csv("data_all_mountains.csv", index=False)

    # save data in s3 bucket
    bucket = os.environ.get("S3_BUCKET")
    csv_buffer = StringIO()
    data_all_mountains.to_csv(csv_buffer, index=False)
    s3_resource = boto3.resource('s3')
    s3_resource.Object(bucket, 'data_all_mountains.csv').put(Body=csv_buffer.getvalue())

    print("processing complete")

