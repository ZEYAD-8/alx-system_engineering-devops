#!/usr/bin/python3
"""
A Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress and
export data in the JSON format.
"""

import json
import requests
import sys


if __name__ == "__main__":
    id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com'
    response_todos = requests.get('{}/todos/?userId={}'.format(url, id))
    response_employee = requests.get('{}/users/{}'.format(url, id))

    todos = response_todos.json()
    username = response_employee.json().get("username")

    formatted_tasks = []
    for todo in todos:
        formatted_tasks.append({'task': todo.get("title"),
                                'completed': todo.get("completed"),
                                'username': username})

    json_list = {id: formatted_tasks}

    filename = "{}.json".format(id)
    with open(filename, "w") as file:
        json.dump(json_list, file)
