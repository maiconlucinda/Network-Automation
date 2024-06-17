
import pickle
import json
def serialise(pythonObj, OutputFile, protocol):

    extension = ""
    if protocol == 'pickle':
        extension = 'dat'
        with open(f"archives/{OutputFile}.{extension}", 'wb') as f:
            pickle.dump(pythonObj, f)


    elif protocol == 'json':
        extension = 'json'
        with open(f"archives/{OutputFile}.{extension}", 'w') as f:
            json.dump(pythonObj, f, indent=4)


    else:
        print("The extension is not valid")





def deserialise(inputFile, protocol):  

    extension = ""   
    if protocol == "pickle":
        extension = "dat"
        with open(f"archives/{inputFile}.{extension}", 'rb') as f:
            obj = pickle.load(f)      
            print(obj)


    if protocol == "json":
        extension = "json"
        with open(f"archives/{inputFile}.{extension}", 'r') as f:
            obj = json.load(f)
            print(obj)






# people = {"Matheus" : [25, "Poland", 99448512], "Fernando": [35, "Romenia", 98567432], "Pablo": [40, "Spain", 98756235]}
# serialise(people, "people", 'json')

deserialise("people", 'pickle')

