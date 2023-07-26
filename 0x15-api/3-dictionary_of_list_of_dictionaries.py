#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Python script to export data in the JSON format
"""
from json import dump
from requests import get


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users/'
    message = get(url)
    users = message.json()

    dict = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        url = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos/'
        message = get(url)
        tasks = message.json()
        dict[user_id] = []
        for task in tasks:
            dict[user_id].append({
                                        "task": task.get('title'),
                                        "completed": task.get('completed'),
                                        "username": username
                                        })
    with open('todo_all_employees.json', 'w') as file:
        dump(dict, file)
