import json


def readJsonFile(fileName):
    data = ""
    try:
        with open(fileName) as json_file:
          data = json.load(json_file)
          print('successss')
    except IOError:
        print("Could not read file")
    return data

# readJsonFile('insulin.json')