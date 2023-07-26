#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This Python script uses the REST API,
for a given employee ID, returns information
about his/her TODO list progress.
"""

import requests
from sys import argv
import json

def fetch_todo_progress(user_id):
    """
    Fetches the user's TODO list progress.

    Args:
        user_id (str): The employee ID to fetch TODO list for.

    Returns:
        dict: Dictionary containing the employee's TODO list progress.
    """
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    res = requests.get(url)
    user_dict = res.json()
    username = user_dict.get("username")

    url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
    res = requests.get(url)
    tasks = res.json()

    task_list = []
    for task in tasks:
        task_list.append({
            "username": username,
            "task": task.get('title'),
            "completed": task.get('completed')
        })

    return {user_id: task_list}

def main():
    """
    Main function to fetch all employees' TODO list progress and store it in a JSON file.
    """
    all_employees_data = {}
    for user_id in argv[1:]:
        employee_data = fetch_todo_progress(user_id)
        all_employees_data.update(employee_data)

    with open('todo_all_employees.json', 'w') as file:
        json.dump(all_employees_data, file)

if __name__ == "__main__":
    main()
