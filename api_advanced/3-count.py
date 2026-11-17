#!/usr/bin/python3
"""
3-count
Recursively queries the Reddit API, parses the titles of all hot articles
and prints a sorted count of the given keywords.
"""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Print a sorted count of keywords found in hot post titles.

    Prints nothing if the subreddit is invalid or no keywords match.
    """
    if counts is None:
        counts = {}

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu-scripting.api_advanced:v1.0 "
                             "(by /u/kethia_keza)"}
    params = {"limit": 100}
    if after:
        params["after"] = after

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False, timeout=10)
        if response.status_code != 200:
            return
        data = response.json().get("data", {})
    except (requests.RequestException, ValueError):
        return

    keywords = [w.lower() for w in word_list]
    for child in data.get("children", []):
        title = child.get("data", {}).get("title", "")
        for word in title.lower().split():
            if word in keywords:
                counts[word] = counts.get(word, 0) + keywords.count(word)

    after = data.get("after")
    if after is not None:
        return count_words(subreddit, word_list, after, counts)

    for word, count in sorted(counts.items(), key=lambda x: (-x[1], x[0])):
        print("{}: {}".format(word, count))
