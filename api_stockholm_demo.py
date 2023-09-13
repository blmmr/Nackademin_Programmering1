import requests
import json

url = "https://54qhf521ze.execute-api.eu-north-1.amazonaws.com/weather/stockholm/"

r = requests.get(url) #fetching into
response_string = r.text #taking info from the website and saving it as text
response_dictionary = json.loads(r.text) #turning this into a dict

print(response_dictionary)
