#!/usr/bin/python3
"""
Exports to-do list information of all employees to JSON format.

This script fetches the user information and to-do lists for all employees
from the JSONPlaceholder API and exports the data to a JSON file.
"""

import json
import requests


def fetch_user_data():
    """Fetch user information and to-do lists for all employees."""
    try:
        # Base URL for the JSONPlaceholder API
        url = "https://jsonplaceholder.typicode.com/"

        # Fetch the list of all users (employees)
        users = requests.get(url + "users").json()

        # Create a dictionary containing to-do list information of all employees
        data_to_export = {}
        for user in users:
            user_id = user["id"]
            user_url = f"{url}todos?userId={user_id}"
            todo_list = requests.get(user_url).json()

            data_to_export[user_id] = [
                {
                    "task": todo.get("title"),
                    "completed": todo.get("completed"),
                    "username": user.get("username"),
                }
                for todo in todo_list
            ]

        return data_to_export

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None


def export_to_json(data_to_export):
    """Export data to JSON file."""
    try:
        with open("todo_all_employees.json", "w") as jsonfile:
            json.dump(data_to_export, jsonfile, indent=4)
        print("Data exported successfully to 'todo_all_employees.json'")
    except Exception as e:
        print(f"Error exporting data to JSON: {e}")


if __name__ == "__main__":
    data_to_export = fetch_user_data()
    if data_to_export:
        export_to_json(data_to_export)
    else:
        print("Failed to fetch data. Please check your internet connection and try again.")
