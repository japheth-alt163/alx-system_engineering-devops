#!/usr/bin/python3
"""
Exports to-do list information for a given employee ID to JSON format.

This script takes an employee ID as a command-line argument and exports
the corresponding user information and to-do list to a JSON file.
"""

import json
import requests
import sys


def fetch_user_info(user_id):
    """Fetch user information from the API."""
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)
    response.raise_for_status()  # Raise exception for failed requests
    return response.json()


def fetch_user_todos(user_id):
    """Fetch the to-do list items associated with the given user ID."""
    url = "https://jsonplaceholder.typicode.com/todos"
    params = {"userId": user_id}
    response = requests.get(url, params=params)
    response.raise_for_status()  # Raise exception for failed requests
    return response.json()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 {} <user_id>".format(sys.argv[0]))
        sys.exit(1)

    user_id = sys.argv[1]

    try:
        user_info = fetch_user_info(user_id)
        username = user_info.get("username")
        user_todos = fetch_user_todos(user_id)
        
        data_to_export = {
            user_id: [
                {
                    "task": todo["title"],
                    "completed": todo["completed"],
                    "username": username
                }
                for todo in user_todos
            ]
        }

        filename = f"{user_id}.json"
        with open(filename, "w") as jsonfile:
            json.dump(data_to_export, jsonfile, indent=4)
        print(f"Data exported to {filename} successfully.")
    
    except requests.RequestException as e:
        print("Error occurred during API request:", e)
        sys.exit(1)
