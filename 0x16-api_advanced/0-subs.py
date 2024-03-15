#!/usr/bin/python3
"""
Function that queries the Reddit API and
returns the number of subscribers.
"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subs, 0 if the given subreddit is invalid."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'MyBot/0.1'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
