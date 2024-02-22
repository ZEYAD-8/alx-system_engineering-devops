#!/usr/bin/python3
import requests
import sys


if __name__ == "__main__":
    id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com'
    response_todos = requests.get('{}/todos/?userId={}'.format(url, id))
    response_employee = requests.get('{}/users/{}'.format(url, id))

    todos = response_todos.json()
    employee = response_employee.json()

    employee_name = employee.get('name')

    completed_tasks = [todo.get('title')
                       for todo in todos
                       if todo.get('completed') is True]

    print('Employee {} is done with tasks({}/{}):'
          .format(employee_name, len(completed_tasks), len(todos)))
    for task in completed_tasks:
        print('\t {}'.format(task))
