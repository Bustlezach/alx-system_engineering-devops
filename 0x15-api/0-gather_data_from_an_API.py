#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This Python script uses the REST API,
for a given employee ID, returns information
about his/her TODO list progress.
"""

import requests
from sys import argv


if __name__ == "__main__":
    """
    Main function to fetch employee's TODO list progress and display it.
    """
    user_id = argv[1]
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    res = requests.get(url)
    user_dict = res.json()
    name = user_dict.get("name")

    url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
    res = requests.get(url)
    tasks = res.json()
    done = 0
    task_done = []

    for task in tasks:
        if task.get("completed"):
            task_done.append(task)
            done += 1

    print(f"Employee {name} is done with tasks({done}/{len(tasks)}):")
    for task in task_done:
        print(f"\t{task.get('title')}")
