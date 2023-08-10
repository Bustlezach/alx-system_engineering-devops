#!/usr/bin/python3
"""
A recursive function that queries the Reddit API,
parses the title of all hot articles, and prints a sorted
count of given keywords (case-insensitive, delimited by spaces.
Javascript should count as javascript, but java should not)
"""
import requests


def count_words(subreddit, list_word, ins={}, after="", count=0):
    """Prints counts of given words found in hot posts of a given subreddit.

    Args:
        subreddit (str): The subreddit to search.
        list_word (list): The list of words to searched in post titles.
        ins (obj): Key/value pairs of words.
        after (str): parameter of next page of the API results.
        count (int): parameter of results matched thus far.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bustlezee)"
    }
    params = {
        "limit": 25,
        "after": after,
        "count": count
    }
    message = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    try:
        res = message.json()
        if message.status_code == 404:
            raise Exception
    except Exception:
        print("")
        return

    res = res.get("data")
    after = res.get("after")
    count += res.get("dist")
    for i in res.get("children"):
        title = i.get("data").get("title").lower().split()
        for word in list_word:
            if word.lower() in title:
                times = len([t for t in title if t == word.lower()])
                if ins.get(word) is None:
                    ins[word] = times
                else:
                    ins[word] += times

    if after is None:
        if len(ins) == 0:
            print("")
            return
        ins = sorted(ins.items(), key=lambda kv: (-kv[1], kv[0]))
        [print("{}: {}".format(k, v)) for k, v in ins]
    else:
        count_words(subreddit, list_word, ins, after, count)
