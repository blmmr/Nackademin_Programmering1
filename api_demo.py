import requests

# Define the API endpoint URL
url = "https://jsonplaceholder.typicode.com/posts/1"

# Send an HTTP GET request to the API
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    
    # Display the fetched data
    print("User ID:", data["userId"])
    print("Title:", data["title"])
    #print("Body:", data["body"])

else:
    print("Failed to fetch data from the API")
