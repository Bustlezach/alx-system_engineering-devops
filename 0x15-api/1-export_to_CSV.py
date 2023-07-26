#!/usr/bin/python3

"""
This Python script uses the REST API,
for a given employee ID, returns information
about his/her TODO list progress and stores it in a CSV file.
"""

import csv
import requests
from sys import argv

def fetch_todo_progress(user_id):
    """
    Fetches the user's TODO list progress and stores it in a CSV file.

    Args:
        user_id (str): The employee ID to fetch TODO list for.

    Returns:
        None
    """
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    res = requests.get(url)
    user_dict = res.json()
    username = user_dict.get("username")

    url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
    res = requests.get(url)
    tasks = res.json()

    field_names = [
        'USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE'
    ]
    result = []

    for task in tasks:
        result.append({
            'USER_ID': user_id,
            'USERNAME': username,
            'TASK_COMPLETED_STATUS': task.get('completed'),
            'TASK_TITLE': task.get('title')
        })

    with open(f'{user_id}.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writerows(result)

if __name__ == "__main__":
    user_id = argv[1]
    fetch_todo_progress(user_id)
