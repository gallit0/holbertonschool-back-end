#!/usr/bin/python3
"""API"""
from sys import argv
import json
import requests

if __name__ == '__main__':
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    u = requests.get('https://jsonplaceholder.typicode.com/users/' + argv[1])
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

    print("Employee {} is done with tasks".format(EMPLOYEE_NAME), end='')
    print('({}/'.format(NUMBER_OF_DONE_TASKS), end='')
    print('{}):'.format(TOTAL_NUMBER_OF_TASKS), end='\n     ')
    print('\n     '.join(done))
