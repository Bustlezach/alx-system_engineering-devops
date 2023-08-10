#!/usr/bin/python3

"""
This script queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bustlezee)"
    }
    message = requests.get(url, headers=headers, allow_redirects=False)
    if message.status_code == 404:
        return 0
    res = message.json().get("data")
    return res.get("subscribers")
