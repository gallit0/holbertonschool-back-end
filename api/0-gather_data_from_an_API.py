#!/usr/bin/python3
"""API"""
import requests
from sys import argv

src = 'https://jsonplaceholder.typicode.com/'

if __name__ == '__main__':
    todos = requests.get(src + "todos?userId=" + argv[1]).json()
    u = requests.get(src + 'users/' + argv[1]).json()
    EMPLOYEE_NAME = u['name']
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    done = []

    for i in list(todos):
        if int(i['userId']) == int(argv[1]):
            if i['completed'] is True:
                done.append(i['title'])
                NUMBER_OF_DONE_TASKS += 1
            TOTAL_NUMBER_OF_TASKS += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(u["name"], len(done), len(todos)))
    print("\n".join("\t {}".format(j) for j in done))
