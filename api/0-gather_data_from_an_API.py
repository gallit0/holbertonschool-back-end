#!/usr/bin/python3
"""API"""
import requests
from sys import argv
import json

if __name__ == '__main__':
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    u = requests.get(f'https://jsonplaceholder.typicode.com/users/{argv[1]}')
    todos_dict = json.loads(todos.text)
    user_dict = json.loads(u.text)
    EMPLOYEE_NAME = user_dict['name']
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    done = []
    for i in list(todos_dict):
        if int(i['userId']) == int(argv[1]):
            if i['completed'] is True:
                done.append(i['title'])
                NUMBER_OF_DONE_TASKS += 1
            TOTAL_NUMBER_OF_TASKS += 1

    print(f"Employee {EMPLOYEE_NAME} is done with tasks", end='')
    print(f'({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS})', end='\n\t ')
    print('\n\t '.join(done))
