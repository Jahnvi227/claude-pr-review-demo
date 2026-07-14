import json
import os
import requests



with open("claude-review.json") as f:

    findings = json.load(f)



if not findings:

    print("No Claude findings")

    exit(0)



comments = []



for item in findings:


    comments.append({

        "path": item["file"],

        "line": item["line"],

        "side": "RIGHT",

        "body": f"""
## {item['severity'].upper()}

{item['finding']}


### Suggested Fix

{item['suggested_fix']}
"""

    })



payload = {

    "event": "COMMENT",

    "comments": comments

}



repo = os.environ["REPOSITORY"]

pr = os.environ["PR_NUMBER"]

token = os.environ["GH_TOKEN"]



url = f"https://api.github.com/repos/{repo}/pulls/{pr}/reviews"



headers = {

    "Authorization": f"Bearer {token}",

    "Accept": "application/vnd.github+json"

}



response = requests.post(

    url,

    headers=headers,

    json=payload

)



print(response.status_code)

print(response.text)



response.raise_for_status()