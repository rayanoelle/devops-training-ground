import json
with open('friends.json','rt') as f:
    obj = json.load(f)
    print(type(obj))
    print(obj)