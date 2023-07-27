#!/usr/bin/python3

"""
Fetches information about all employees and exports it to a JSON file.

API: https://jsonplaceholder.typicode.com/
"""

import json
import requests
import sys

API = "https://jsonplaceholder.typicode.com"


if __name__ == "__main__":
    # get employees details
    response = requests.get("{}/users/".format(API))
    if not response.ok:
        sys.exit()
    employees = response.json()

    data = {}

    # get employee todos
    for employee in employees:
        employee_id = employee.get("id")
        response = requests.get("{}/todos?userId={}".format(
            API, employee_id
        ))
        if not response.ok:
            sys.exit()
        employee_todos = response.json()

        # store details in variables
        username = employee.get('username')

        todos = []
        for todo in employee_todos:
            todos.append({
                "username": username,
                "task": todo.get('title'),
                "completed": todo.get('completed')
            })
        data["{}".format(employee_id)] = todos

    with open("todo_all_employees.json", 'w') as json_file:
        json_file.write(json.dumps(data))
