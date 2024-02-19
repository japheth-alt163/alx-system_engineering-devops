#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""

import csv
import requests
import sys


def fetch_user_info(user_id):
    """Fetch user information from the API."""
    url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    response = requests.get(url)
    return response.json()


def fetch_user_todos(user_id):
    """Fetch the to-do list items associated with the given user ID."""
    url = "https://jsonplaceholder.typicode.com/todos"
    params = {"userId": user_id}
    response = requests.get(url, params=params)
    return response.json()


def export_to_csv(user_id, username, todos):
    """Export to-do list information to a CSV file."""
    filename = "{}.csv".format(user_id)
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for todo in todos:
            writer.writerow([user_id, username, todo["completed"], todo["title"]])
    print("Data exported to {} successfully.".format(filename))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 {} <user_id>".format(sys.argv[0]))
        sys.exit(1)

    user_id = sys.argv[1]

    try:
        user_info = fetch_user_info(user_id)
        username = user_info.get("username")
        user_todos = fetch_user_todos(user_id)
        export_to_csv(user_id, username, user_todos)
    except requests.RequestException as e:
        print("Error occurred during API request:", e)
        sys.exit(1)
