#!/usr/bin/python3
"""
This script retrieves information about an employee's TODO list progress
using a REST API.
"""

import sys
import requests


def get_employee_todo_progress(employee_id):
    """
    Retrieves and displays the TODO list progress for a given employee.

    Args:
        employee_id (int): The ID of the employee.
    """
    url = "https://jsonplaceholder.typicode.com/todos?userId=" + str(employee_id)
    response = requests.get(url)
    todos = response.json()

    if not todos:
        print("No TODO list found for the specified employee ID.")
        return

    completed_tasks = [todo for todo in todos if todo['completed']]
    total_tasks = len(todos)
    num_completed_tasks = len(completed_tasks)
    employee_name = todos[0]['userId']

    print(f"Employee {employee_name} is done with tasks({num_completed_tasks}/{total_tasks}):")

    for todo in completed_tasks:
        print(f"\t{todo['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
