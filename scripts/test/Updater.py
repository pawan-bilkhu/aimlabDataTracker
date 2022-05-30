import settings
import json


def update_json(read_path, write_path, field, value, start_index):
    if start_index == 0:
        with open(read_path, 'r') as file:
            data = json.load(file)
        # print(data[0])
        for entry in data:
            entry[field] += value
        # print(data[0])
        with open(write_path, 'w') as file:
            json.dump(data, file, indent=4)


if __name__ == '__main__':
    read_path = settings.joinpath(settings.DATA, 'cleanData/cleanTaskData(newCom).json')
    write_path = settings.joinpath(settings.DATA, 'cleanData/cleanTaskData(newCom_adjustedId).json')
    update_json(read_path, write_path, "taskId", -1, 0)