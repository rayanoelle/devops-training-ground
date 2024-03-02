import requests
import json
response = requests.get('https://jsonplaceholder.typicode.com/todos', verify=False)
todos = json.loads(response.text)
for task in  todos:
    if task['completed'] == True:
        print(task)