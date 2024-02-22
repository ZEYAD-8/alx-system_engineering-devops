#!/usr/bin/python3
"""
A Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress and
export data in the CSV format.
"""

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

    with open('{}.csv'.format(eid), 'w') as f:
        for task in tasks:
            f.write('"{}","{}","{}","{}"\n'
                    .format(eid, uname, task.get('completed'),
                            task.get('title')))
