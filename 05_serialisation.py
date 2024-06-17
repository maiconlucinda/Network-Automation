
# SERIALISATION WITH PICKLE
friends = {"Matheus" : [25, "Poland", 99448512], "Fernando": [35, "Romenia", 98567432], "Pablo": [40, "Spain", 98756235]}

# It does not work because a dict can not be saved into a file, it has to be a string
# with open('archives/friends.txt', 'w') as friendslist:
#     friendslist.write(friends)



# How to encode a Python object into a stream of bytes and save thses bytes into a file
import pickle

friends = {"Matheus" : [25, "Poland", 99448512], "Fernando": [35, "Romenia", 98567432], "Pablo": [40, "Spain", 98756235]}

with open('archives/friends.dat', 'wb') as f:

    # First argument is the dict and the second one is the file
    pickle.dump(friends, f)




# How to decode the file 
with open('archives/friends.dat', 'rb') as f:
    obj = pickle.load(f)

    print(type(obj))
    print(obj)




# We can serialise a lot of dicts at the same time, we can for example use a tuple
friends1 = {"Matheus" : [25, "Poland", 99448512], "Fernando": [35, "Romenia", 98567432], "Pablo": [40, "Spain", 98756235]}
friends2 = {"Joaquina" : [25, "Poland", 99448512], "Pedro": [35, "Romenia", 98567432], "Guilherme": [40, "Spain", 98756235]}

friends = (friends1, friends2)


with open('archives/friends.dat', 'wb') as f:

    # First argument is the dict and the second one is the file
    pickle.dump(friends, f)




# How to decode the file 
with open('archives/friends.dat', 'rb') as f:
    obj = pickle.load(f)

    print(type(obj))
    print(obj)
print('#' * 80)



# SERIALISATION WITH JSON
import json
friends = {"Matheus" : [25, "Poland", 99448512], "Fernando": [35, "Romenia", 98567432], "Pablo": [40, "Spain", 98756235]}

with open('archives/friends.json', 'w') as f:
    # If we have a lot of information, we can use indent=, it will indent the return in a better format
    json.dump(friends, f, indent=4)

# If we want only a string representation, we can use:

json_string = json.dumps(friends, indent=4)
print(json_string)






# DESERIALISATION
import json
with open('archives/friends.json', 'rt') as f:
    obj = json.load(f)
    print(type(obj))
    print(obj)