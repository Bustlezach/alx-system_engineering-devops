import requests
from sys import argv

user_id = argv[1]
url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
res = requests.get(url)
r_dict = res.json()
name = r_dict.get("name")
#print(name)

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
