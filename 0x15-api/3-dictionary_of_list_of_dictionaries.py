#!/usr/bin/python3
"""
A Python script that, using this REST API, returns
all information all users' TODO list progress
and export data in the JSON format.
"""

import json
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'
    response_todos = requests.get('{}/todos/'.format(url))
    response_employees = requests.get('{}/users/'.format(url))

    todos = response_todos.json()
    employees = response_employees.json()

    json_list = {}
    for employee in employees:
        employee_tasks = []
        id = employee.get("id")
        username = employee.get("username")
        for todo in todos:
            if todo.get("userId") == id:
                employee_tasks.append({'task': todo.get("title"),
                                       'completed': todo.get("completed"),
                                       'username': username})

        json_list[id] = employee_tasks

    filename = "todo_all_employees.json"
    with open(filename, "w") as file:
        json.dump(json_list, file)
