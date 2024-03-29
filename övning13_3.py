import requests
import json
import pprint

def UI():
    print("--- ARTIST DB ---")
    print("Ariana Grande")
    print("Avicii")
    print("Blink -182")
    print("Brad Paisley")
    print("Ed Sheeran")
    print("Imagine Dragons")
    print("Maroon 5")
    print("Scorpions")
    print("-----------------")

url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"

r = requests.get(url) #fetching into
response_string = r.text #taking info from the website and saving it as text
response_dictionary = json.loads(r.text) #turning this into a dict

UI()
userArtist = input("Input the name of the artist: ")

for artist in response_dictionary["artists"]:
    if artist["name"] == userArtist:
        artistId = artist["id"]
        break

artist_url = f"https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/{artistId}"
artist_api = requests.get(artist_url) #fetching into
artist_string = artist_api.text #taking info from the website and saving it as text
artist_dictionary = json.loads(artist_api.text) #turning this into a dict

pprint.pprint(artist_dictionary)