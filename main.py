import requests
import json

events_dict = {
    "CreateEvent": lambda event: print(f"- Created {event["repo"]["name"]}"),
    "PushEvent": lambda event: print(f"- Pushed commit to {event["repo"]["name"]}"),
    "WatchEvent": lambda event: print(f"- Viewed {event["repo"]["name"]}"),
    "ForkEvent": lambda event: print(f"- Forked {event["repo"]["name"]}"),
    "IssuesEvent": lambda event: print(f"- Opened a new issue in {event["repo"]["name"]}"),
}

username = input("Github Username: ")
url = f"https://api.github.com/users/{username}/events"

response = requests.get(url)
events = response.json()

with open('reponse.json', "w") as file:
    json.dump(events, file, indent=4)

while events["message"] != "Not Found":
    for event in events:
        if event["type"] in events_dict:
            events_dict[event["type"]](event)
        else:
            print(f"Event: {event["type"]}")

print("User Not Found")