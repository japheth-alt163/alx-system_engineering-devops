#!/usr/bin/python3
"""
Recursive function that queries the Reddit API, parses the
titles of all hot articles, and prints a sorted count of given
keywords.
"""

import requests


def count_words(subreddit, word_list, after=None, counts={}):
    """
    Recursive function that queries the Reddit API, parses the
    titles of all hot articles, and prints a sorted count of given
    keywords.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100, 'after': after}

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
                title = post['data']['title'].lower()
                for word in word_list:
                    if word.lower() in title:
                        counts[word.lower()] = counts.get(word.lower(), 0) + 1
            after = data.get('after')
            if after:
                return count_words(subreddit, word_list, after, counts)
            else:
                sorted_counts = sorted(
                    counts.items(),
                    key=lambda x: (-x[1], x[0]))
                for word, count in sorted_counts:
                    print(f"{word}: {count}")
        else:
            return None
    else:
        return None


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'"
              .format(sys.argv[0]))
    else:
        count_words(sys.argv[1], sys.argv[2].split())
