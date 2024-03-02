import pickle
friends = {"dan":[20,"london", 10000], "maria": [25,'tehran', 5245]}
with open('friends.dat', 'wb') as f:
    pickle.dump(friends,f)
with open('friends.dat','rb') as f:
    obj = pickle.load(f)
    print(type(obj))
    print(obj)