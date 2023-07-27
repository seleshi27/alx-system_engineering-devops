#!/usr/bin/python3

"""
Fetches and displays information about an employee

API: https://jsonplaceholder.typicode.com/
"""
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
    name = employee_details.get('name')
    num_of_todos = len(employee_todos)
    completed_todos = list(filter(
        lambda t: t.get("completed"), employee_todos))

    print("Employee {} is done with tasks({}/{}):".format(
        name, len(completed_todos), num_of_todos
    ))
    for todo in completed_todos:
        print("\t {}".format(todo.get('title')))
