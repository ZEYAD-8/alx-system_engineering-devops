#!/usr/bin/python3
"""
A Python script that, using this REST API, returns
all information all users' TODO list progress
and export data in the JSON format.
"""

import json
import requests


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(url)
    users = response.json()

    dic = {}
    for user in users:
        userId = user.get('id')
        uname = user.get('username')

        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(userId)
        url = url + '/todos/'

        response = requests.get(url)
        tasks = response.json()
        dic[userId] = []

        for task in tasks:
            dic[userId].append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": uname
            })

    with open('todo_all_employees.json', 'w') as f:
        json.dump(dic, f)
