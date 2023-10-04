import json
from bs4 import BeautifulSoup




# returns JSON object as
# a dictionary
# data = json.load(f)

with open('responses/matterhorn.json', encoding="utf8") as jsonFile:
    data = json.load(jsonFile)

# print(data)
# print(data['elevations'].keys())
# print(data['elevations']['4478'].keys())
# print(data['elevations']['4478']['period_types'].keys())
# print(data['elevations']['4478']['period_types']['p'].keys())
# print(data['elevations']['4478']['period_types']['p']['table'])


soup = BeautifulSoup(data['elevations']['4478']['period_types']['p']['table'], 'html.parser')
# print(soup.prettify())
# print(soup.find_all("data-row=\"summary\""))
# print(soup.find(id="forecast-table"))

dates = []
# get days
for day in soup.find_all(class_='forecast__table-days-content'):
    text = day.get_text()
    text_no_spaces = text.strip()
    text_no_line_breaks = text_no_spaces.replace("\n", "")
    text_single_spaces = " ".join(text_no_line_breaks.split())
    dates.append(text_single_spaces)

# print(dates)

times = []
start_index = 0

date_times = []
# get times
for time in soup.find_all(class_="forecast__table-time"):
    text = time.get_text()
    text_no_spaces = text.strip()
    text_no_line_breaks = text_no_spaces.replace("\n", "")
    text_single_spaces = " ".join(text_no_line_breaks.split())
    text_list = text_single_spaces.split(" ")
    for val in text_list:
        if val not in {"night", "AM", "PM"}:
            continue
        date_times.append(dates[start_index] + " " + val)
        if val == "night":
            start_index += 1
# print(date_times)
# print(len(date_times))

weather = []
# get weather text
for weather in soup.find_all(class_="forecast__table-summary"):
    text = weather.get_text()
    text_no_spaces = text.strip()
    text_no_line_breaks = text_no_spaces.split("\n")
    formated_text = [x.strip() for x in text_no_line_breaks]
    final_text = [x for x in formated_text if x.strip() != ""]
    weather = final_text

wind = []
for val in soup.find_all(class_="forecast__table-wind-container"):
    text = val.get_text()
    text_no_spaces = text.strip()
    wind.append(text_no_spaces)

for index, date in enumerate(date_times):
    print(date + " " + weather[index] + " wind " + wind[index])