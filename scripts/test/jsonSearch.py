import settings
import json

path = settings.joinpath(settings.DATA, 'cleanData/cleanTaskData.json')

with open(path, 'r') as file:
    data = json.load(file)


# Testing JSON search task name
for entry in data:
    if entry['taskName'] == 'gridshot':
        print(entry)