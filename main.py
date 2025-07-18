import requests
import json

username = input("Github Username: ")
url = f"https://api.github.com/users/{username}/events"

response = requests.get(url)
events = response.json()

with open('reponse.json', "w") as file:
    json.dump(events, file, indent=4)

for event in events:
    if event["type"] == "CreateEvent":
        print(f"- Created {event["repo"]["name"]}")
    elif event["type"] == "PushEvent":
        print(f"- Pushed {event["payload"]["size"]} commits to {event["repo"]["name"]}")
    else:
        print(event["type"])
        print(event["repo"]["name"])

print()