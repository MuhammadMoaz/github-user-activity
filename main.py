import requests
import json

events_dict = {
    "CreateEvent": lambda event: print(f"- Created {event["repo"]["name"]}"),
    "PushEvent": lambda event: print(f"- Pushed {event["payload"]["size"]} commits to {event["repo"]["name"]}"),
    "WatchEvent": lambda event: print(f"- Viewed {event["repo"]["name"]}"),
    "CommitCommentEvent": lambda event: print(""),
    "DeleteEvent": lambda event: print(""),
    "ForkEvent": lambda event: print(""),
    "GollumEvent": lambda event: print(""),
    "IssueCommentEvent": lambda event: print(""),
    "IssuesEvent": lambda event: print(""),
    "MemberEvent": lambda event: print(""),
    "PublicEvent": lambda event: print(""),
    "PullRequestEvent": lambda event: print(""),
    "PullRequestReviewEvent": lambda event: print(""),
    "PullRequestReviewCommentEvent": lambda event: print(""),
    "PullRequestReviewThreadEvent": lambda event: print(""),
    "ReleaseEvent": lambda event: print(""),
    "SponsorshipEvent": lambda event: print("")
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