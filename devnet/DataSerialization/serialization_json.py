import json
friends = {"dan":[20,"london", 10000], "maria": [25,'tehran', 5245]}
with open('friends.json','w') as f:
    json.dump(friends, f, indent=4)
json_string = json.dumps(friends)
print(json_string)