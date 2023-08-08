#!/usr/bin/python3

"""
This script queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit
"""

import requests


def top_ten(subreddit):
    """This function prints the top ten hot post"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Custom User-Agent'}
    params = {'limit': 10}
    message = requests.get(url, headers=headers, params=params, allow_redirects=False)
    res = message.json()

    content = []

    for post in res['data']['children']:
        content.append(post['data']['title'])

    for i in content:
        print(i)
