import requests
import json

userInteger = input("Write down an integer: ")

userInteger = int(userInteger)

url = f"https://4bbh01oqwj.execute-api.eu-north-1.amazonaws.com/numcheck?integer={userInteger}"

r = requests.get(url) #fetching into
response_string = r.text #taking info from the website and saving it as text
response_dictionary = json.loads(r.text) #turning this into a dict

#print(response_dictionary)

for i, x in response_dictionary.items():
  print(i, " : ", x)