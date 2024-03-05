#!/usr/bin/python3
"""
Recursively queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[]):
    """
    Recursively queries the Reddit API and returns
    a list containing the titles of all hot articles for a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100}

    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False
        )

    if response.status_code == 200:
        data = response.json().get('data', {})
        children = data.get('children', [])
        if children:
            for post in children:
                hot_list.append(post['data']['title'])
            after = data.get('after')
            if after:
                return recurse(subreddit, hot_list)
            else:
                return hot_list
        else:
            return hot_list
    else:
        return None


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")
