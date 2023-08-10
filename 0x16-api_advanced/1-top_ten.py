#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """This function prints the top ten hot post"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'linux:0x16.api.advanced:v1.0.0 (by /u/bustlezee)'}
    params = {'limit': 10}
    message = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if message.status_code == 404:
        print("None")
        return
    res = message.json().get("data")
    [print(i.get("data").get("title")) for i in res.get("children")]
