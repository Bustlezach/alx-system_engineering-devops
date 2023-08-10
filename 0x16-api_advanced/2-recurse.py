#!/usr/bin/python3
"""
This script queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """This function recursively prints the article titles."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /bustlezee)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    message = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if message.status_code == 404:
        return None

    res = message.json().get("data")
    after = res.get("after")
    count += res.get("dist")
    for i in res.get("children"):
        hot_list.append(i.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
