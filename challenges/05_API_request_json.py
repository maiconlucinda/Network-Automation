import json
import requests

r = requests.get('https://jsonplaceholder.typicode.com/todos')

#print(r.text)
todos = json.loads(r.text)

print(type(todos))
# print(todos)


for task in todos:
    if task['completed'] == True:
        print(task)

