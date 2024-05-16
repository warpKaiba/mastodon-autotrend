# autotrend.py
# This script automatically approves all trendable posts that are waiting to be approved
# Your application access token needs admin:read and admin:write for this to work
# (Mastodon does not provide any more specific permission groups regarding trends)

import requests, json, hashlib, time


# Your mastodon instance's domain
domainName = "mastodon.com"

# Your mastodon applications's access token
accessToken = "changeme"

headers = {"Authorization": "Bearer " + accessToken}


def getTrending():
    url = 'https://'+domainName+'/api/v1/admin/trends/statuses/'
    r = requests.get(url, headers=headers)

    if r.status_code != 200:
        print("Failed to get trends")
        return None

    r = r.json()
    for post in r:
        approveTrending(post['id'])

def approveTrending(status_id):
    url = 'https://'+domainName+'/api/v1/admin/trends/statuses/'+status_id+'/approve'
    r = requests.post(url, headers=headers)

    if r.status_code != 200:
        print("Failed to approve trend")
        return None
    print(r)


getTrending()
