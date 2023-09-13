import requests
import json
import pprint

print("Enter the name of the city for which you want forecasts:")
userCity = input("> ")

url = f"https://54qhf521ze.execute-api.eu-north-1.amazonaws.com/weather/{userCity}"

r = requests.get(url) #fetching into
response_string = r.text #taking info from the website and saving it as text
response_dictionary = json.loads(r.text) #turning this into a dict

target_dictionary = response_dictionary['forecasts']
pprint.pprint(target_dictionary)

for i in target_dictionary:
    date = i['date']
    forecast = i['forecast']
    print(f"Date: {date}, Forecast: {forecast}")
