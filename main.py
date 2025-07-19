import requests
import json

events_dict = {
    "CreateEvent": lambda event: print(f"- Created {event["repo"]["name"]}"),
    "PushEvent": lambda event: print(f"- Pushed {event["payload"]["size"]} commits to {event["repo"]["name"]}"),
    "WatchEvent": lambda event: print(f"- Viewed {event["repo"]["name"]}")
}

username = input("Github Username: ")
url = f"https://api.github.com/users/{username}/events"

response = requests.get(url)
events = response.json()

with open('reponse.json', "w") as file:
    json.dump(events, file, indent=4)

for event in events:
    if event["type"] in events_dict:
        events_dict[event["type"]](event)
    else:
        print(f"Unknown Event Type {event["type"]}")