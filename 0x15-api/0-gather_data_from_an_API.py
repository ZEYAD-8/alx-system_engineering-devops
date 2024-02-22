#!/usr/bin/python3
"""
A Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
from sys import argv


if __name__ == '__main__':
    eid = argv[1]
    userUrl = "https://jsonplaceholder.typicode.com/users"
    url = userUrl + "/" + eid

    response = requests.get(url)
    EMPLOYEE_NAME = response.json().get('name')

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()
    totalTasks = len(tasks)

    NUMBER_OF_DONE_TASKS = 0
    tasksList = []

    for task in tasks:
        if task.get('completed'):
            tasksList.append(task)
            NUMBER_OF_DONE_TASKS += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, totalTasks))

    for task in tasksList:
        print("\t {}".format(task.get('title')))