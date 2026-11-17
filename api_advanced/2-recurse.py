#!/usr/bin/python3
"""
2-recurse
Recursively queries the Reddit API and returns a list of the titles
of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """Return a list of titles of all hot posts of a subreddit.

    Returns None if the subreddit is invalid or has no results.
    """
    if hot_list is None:
        hot_list = []

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
            return hot_list or None
        data = response.json().get("data", {})
    except (requests.RequestException, ValueError):
        return hot_list or None

    for child in data.get("children", []):
        hot_list.append(child.get("data", {}).get("title"))

    after = data.get("after")
    if after is None:
        return hot_list or None
    return recurse(subreddit, hot_list, after)
