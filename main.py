import requests
import json

events_dict = {
    "CreateEvent": lambda event: print(f"- Created {event["repo"]["name"]}"),
    "PushEvent": lambda event: print(f"- Pushed commit to {event["repo"]["name"]}"),
    "WatchEvent": lambda event: print(f"- Viewed {event["repo"]["name"]}"),
    "CommitCommentEvent": lambda event: print(f"- Commit Comment"),
    "DeleteEvent": lambda event: print(f"- Deleted ... "),
    "ForkEvent": lambda event: print(f"- Forked ... "),
    "GollumEvent": lambda event: print(f"- Gollum ... "),
    "IssueCommentEvent": lambda event: print(f"- Issued Comment"),
    "IssuesEvent": lambda event: print(f"- Issued ..."),
    "MemberEvent": lambda event: print(f"- Member"),
    "PublicEvent": lambda event: print(f"- Public Event"),
    "PullRequestEvent": lambda event: print(f"- Sent a Pull Request ..."),
    "PullRequestReviewEvent": lambda event: print(f"- Reviewed Pull Request"),
    "PullRequestReviewCommentEvent": lambda event: print(f"- PRRC"),
    "PullRequestReviewThreadEvent": lambda event: print(f"- PRRT"),
    "ReleaseEvent": lambda event: print(f"- Released ..."),
    "SponsorshipEvent": lambda event: print(f"- Sponsored ...")
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