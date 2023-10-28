import requests
import json

def scrape():

    with open("82peaks.json") as peak_names_file:
        peak_names = json.load(peak_names_file)

    print("pulling peaks")
    for peak in peak_names:
        url = "https://www.mountain-forecast.com/peaks/" + peak + "/forecasts/data?elev=all&period_types=p,t,h"
        headers = {"accept": "application/json"}
        res = requests.get(url, headers=headers)
        if res.status_code != 200:
            print("There has been a problem")
            print(peak)
            print(res.status_code)
        json_object = json.dumps(res.json())

        with open("scrape_responses/" + peak + ".json", "w") as outfile:
            outfile.write(json_object)

    print("scraping complete")