#!/usr/bin/python3
"""Script that returns top 10 hot posts of a subreddit"""

import requests


def recurse(subreddit, hot_list=None, after=None):
    """Recursive function that returns a list of top posts"""
    
    if hot_list is None:
        hot_list = []
    endpoint = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {
        'limit': 100,
        'after': after
    }
    headers = {'User-Agent': 'Custom'}
    response = requests.get(endpoint, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        for post in data['data']['children']:
            hot_list.append(post['data']['title'])

        if data['data']['after'] is not None:
            return recurse(subreddit, hot_list, data['data']['after'])
        else:
            return hot_list
    else:
        return None
