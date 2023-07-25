#!/usr/bin/python3
"""
This python script to export data in the CSV format
"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    """Fetch the user ID from command-line arguments"""
    user_id = argv[1]

    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    res = requests.get(url)
    user_dict = res.json()
    username = user_dict.get("username")


    url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
    res = requests.get(url)
    tasks = res.json()

    field_names = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
    result = []


    for task in tasks:
    """Prepare the data for the CSV file"""
        result.append({
            'USER_ID': user_id,
            'USERNAME': username,
            'TASK_COMPLETED_STATUS': task.get('completed'),
            'TASK_TITLE': task.get('title')
        })


    with open(f'{user_id}.csv', 'w', newline='') as csvfile:
    """Write the data to a CSV file named after the user_id"""
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(result)
