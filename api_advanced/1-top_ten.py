#!/usr/bin/python3
"""
1-top_ten
Queries the Reddit API and prints the titles of the first 10 hot posts
for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts of a subreddit.

    Prints None if the subreddit is invalid.
    """
    if not subreddit or not isinstance(subreddit, str):
        print(None)
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu-scripting.api_advanced:v1.0 "
                             "(by /u/kethia_keza)"}
    params = {"limit": 10}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False, timeout=10)
        if response.status_code != 200:
            print(None)
            return
        posts = response.json().get("data", {}).get("children", [])
    except (requests.RequestException, ValueError):
        print(None)
        return

    for post in posts[:10]:
        print(post.get("data", {}).get("title"))
