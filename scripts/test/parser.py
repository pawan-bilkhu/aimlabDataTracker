import json
import settings

rawTaskData = settings.joinpath(settings.DATA, 'rawData/taskData(oldCom).json')


with open(rawTaskData, 'r') as file:
    oldData = json.load(file)
print(oldData)

writePath = settings.joinpath(settings.DATA, 'cleanData/cleanTaskData.json')


with open(writePath, 'w') as file:
    json.dump(oldData, file, indent=4)

