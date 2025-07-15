import requests
import json

username = input("Github Username: ")
url = f"https://api.github.com/users/{username}/events"

response = requests.get(url)
events = response.json()

with open('reponse.json', "w") as file:
    json.dump(events, file, indent=4)

for event in events:
    print(event["type"])
    print(event["repo"]["name"])

print()