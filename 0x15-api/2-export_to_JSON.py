#!/usr/bin/python3
"""
A Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress and
export data in the JSON format.
"""

import json
import requests
from sys import argv


if __name__ == '__main__':
    eid = argv[1]
    userUrl = "https://jsonplaceholder.typicode.com/users"
    url = userUrl + "/" + eid

    response = requests.get(url)
    uname = response.json().get('username')

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()

    dic = {eid: []}
    for task in tasks:
        dic[eid].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": uname
        })

    with open('{}.json'.format(eid), 'w') as f:
        json.dump(dic, f)
