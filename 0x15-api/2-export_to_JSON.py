#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Python script to export data in the JSON format.
"""
from json import dump
from requests import get
from sys import argv


if __name__ == '__main__':
    user_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    message = get(url)
    username = message.json().get('username')

    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)
    message = get(url)
    res = message.json()
    dict = {user_id: []}
    for task in res:
        dict[user_id].append({
                                    "task": task.get('title'),
                                    "completed": task.get('completed'),
                                    "username": username
                                    })
    with open('{}.json'.format(user_id), 'w') as file:
        dump(dict, file)
