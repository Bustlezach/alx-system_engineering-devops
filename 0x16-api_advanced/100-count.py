#!/usr/bin/python3

"""
This script queries the Reddit API, parses the title of all hot articles,
and prints a sorted count of given keywords (case-insensitive, delimited by spaces.
Javascript should count as javascript, but java should not).
"""

import requests
from collections import Counter


def count_words(subreddit, word_list, after=None, word_counter=None):
    """This function recursively print the article titles"""
    if word_counter is None:
        word_counter = Counter()

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Custom User-Agent'}
    params = {'limit': 25, 'after': after}

    message = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if message.status_code == 404:
        return

    res = message.json()

    if 'data' not in res:
        return

    data = res['data']
    after = data['after']

    for post in data['children']:
        title = post['data']['title'].lower()
        for word in word_list:
            if f" {word.lower()} " in f" {title} ":
                word_counter[word.lower()] += 1

    if after:
        count_words(subreddit, word_list, after, word_counter)
    else:
        sorted_words = sorted(word_counter.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_words:
            print(f"{word}: {count}")
