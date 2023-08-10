#!/usr/bin/python3

"""
This script queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'linux:0x16.api.advanced:v1.0.0 (by /u/bustlezee)'}

    message = requests.get(url, headers=headers, allow_redirects=False)
    if message.status_code == 404:
        return 0
    
    response = message.json()
    
    content = {}

    for key, value in response.items():
        content[key] = value

    return content['data']['subscribers']
