#!/usr/bin/python3

"""
Fetches information about an employee and exports it to a JSON file.

API: https://jsonplaceholder.typicode.com/
"""
import json
import requests
import sys

API = "https://jsonplaceholder.typicode.com"


if __name__ == "__main__":
    employee_id = sys.argv[1]
    # get employee details
    response = requests.get("{}/users/{}".format(API, employee_id))
    if not response.ok:
        sys.exit()
    employee_details = response.json()

    # get employee todos
    response = requests.get("{}/todos?userId={}".format(API, employee_id))
    if not response.ok:
        sys.exit()
    employee_todos = response.json()

    # store details in variables
    username = employee_details.get('username')

    todos = []
    data = {"{}".format(employee_id): todos}
    for todo in employee_todos:
        todos.append({
            "task": todo.get('title'),
            "completed": todo.get('completed'),
            "username": username
        })

    with open("{}.json".format(employee_id), 'w') as json_file:
        json_file.write(json.dumps(data))
