import json
import settings

rawTaskData1 = settings.joinpath(settings.DATA, 'rawData/taskData(oldCom).json')
rawTaskData2 = settings.joinpath(settings.DATA, 'rawData/taskData(newCom).json')

with open(rawTaskData1, 'r') as file:
    oldData = json.load(file)
print(oldData)

with open(rawTaskData2, 'r') as file:
    newData = json.load(file)
print(newData)

writePath1 = settings.joinpath(settings.DATA, 'cleanData/cleanTaskData(oldCom).json')
writePath2 = settings.joinpath(settings.DATA, 'cleanData/cleanTaskData(newCom).json')

with open(writePath1, 'w') as file:
    json.dump(oldData, file, indent=4)

with open(writePath2, 'w') as file:
    json.dump(newData, file, indent=4)