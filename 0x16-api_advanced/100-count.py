#!/usr/bin/python3
""" Count it! """

import requests


def count_words(subreddit, word_list, after=None, counts={}):
    """
    Returns the count of appearances of words contained in a given word list
    within the titles of all hot articles for a given subreddit.
    If no results are found for the given subreddit, the function returns None.
    """
    if subreddit is None or not word_list:
        return None

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {
        'limit': 100,
        'after': after
    }
    headers = {'User-Agent': 'Custom-ME'}

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()

        for post in data['data']['children']:
            title = post['data']['title'].lower()
            for word in word_list:
                if word.lower() in title.split():
                    if word.lower() in counts:
                        counts[word.lower()] += 1
                    else:
                        counts[word.lower()] = 1

        if data['data']['after'] is not None:
            after = data['data']['after']
            return count_words(subreddit, word_list, after, counts)
        else:
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
    else:
        return None
