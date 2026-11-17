#!/usr/bin/python3
"""
1-top_ten
Queries the Reddit API and prints the titles of the first 10 hot posts
for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts of a subreddit.

    Returns OK when the subreddit can't be retrieved.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu-scripting.api_advanced:v1.0 "
                             "(by /u/kethia_keza)"}
    params = {"limit": 10}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False, timeout=10)
        if response.status_code != 200:
            return "OK"
        posts = response.json().get("data", {}).get("children", [])
    except (requests.RequestException, ValueError):
        return "OK"

    for post in posts[:10]:
        print(post.get("data", {}).get("title"))
    return "OK"
