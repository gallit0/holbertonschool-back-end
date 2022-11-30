#!/usr/bin/python3
"""API"""
import requests
from sys import argv
import csv

src = 'https://jsonplaceholder.typicode.com/'

if __name__ == '__main__':
    todos = requests.get(src + "todos?userId=" + argv[1]).json()
    u = requests.get(src + 'users/' + argv[1]).json()
    EMPLOYEE_NAME = u['name']
    done = []
    j = 0
    for i in list(todos):
        if int(i['userId']) == int(argv[1]):
            done.append([argv[1], u['name'], i['completed'], i['title']])

    with open('2.csv', 'w') as csvfile:
        sw = csv.writer(csvfile, delimiter=',', lineterminator='\r\n',
                        quoting=csv.QUOTE_ALL)
        for i in done:
            sw.writerow(i)
