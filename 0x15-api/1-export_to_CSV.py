#!/usr/bin/python3
"""
A Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress and
export data in the CSV format.
"""

import csv
import requests
from sys import argv


if __name__ == "__main__":
    id = argv[1]
    url = 'https://jsonplaceholder.typicode.com'
    response_todos = requests.get('{}/todos/?userId={}'.format(url, id)).json()
    response_employee = requests.get('{}/users/{}'.format(url, id)).json()

    username = response_employee.get('username')

    lis_tasks = []
    for todo in response_todos:
        lis_tasks.append([id,
                          username,
                          todo.get('completed'),
                          todo.get('title')])

    filename = "{}.csv".format(id)
    with open(filename, "w") as file:
        writer_object = csv.writer(file)
        writer_object.writerows(lis_tasks)
