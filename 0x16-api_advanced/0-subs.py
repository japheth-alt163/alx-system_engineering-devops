#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers for a given subreddit
"""

import requests

def number_of_subscribers(subreddit):
    """
    Function to fetch the number of subscribers for a subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Custom User Agent'}  # Custom User-Agent header

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except Exception as e:
        print("Error:", e)
        return 0

if __name__ == "__main__":
    subreddit = input("Enter the subreddit name: ")
    print(number_of_subscribers(subreddit))
