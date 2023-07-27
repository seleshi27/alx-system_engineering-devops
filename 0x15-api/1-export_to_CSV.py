#!/usr/bin/python3

"""
Fetches information about an employee and exports it to a CSV file.

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
    username = employee_details.get('username')

    CSV = ""
    for todo in employee_todos:
        title = todo.get('title')
        status = todo.get('completed')
        CSV += '"{}","{}","{}","{}"\n'.format(
            employee_id, username, status, title
        )

    with open("{}.csv".format(employee_id), 'w') as csv_file:
        csv_file.write(CSV)
