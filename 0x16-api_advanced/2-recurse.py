#!/usr/bin/python3
"""
This script queries the Reddit API and returns  a 
list containing the titles of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """This function recursively print the article titles"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Custom User-Agent'}
    params = {'limit': 25, 'after': after}

    message = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if message.status_code == 404:
        return None

    res = message.json()

    if 'data' not in res:
        return None

    data = res['data']
    after = data['after']

    for post in data['children']:
        hot_list.append(post['data']['title'])

    if after:
        return recurse(subreddit, hot_list, after)
    return hot_list
