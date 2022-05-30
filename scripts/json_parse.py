import json
import settings


def clean_parse(read_path, write_path):
    with open(read_path, 'r') as file:
        raw_data = json.load(file)
    print(raw_data)
    with open(write_path, 'w') as file:
        json.dump(raw_data, file, indent=4)


if __name__ == '__main__':
    read_path = settings.joinpath(settings.DATA, 'rawData/taskData.json')
    write_path = settings.joinpath(settings.DATA, 'cleanData/cleanTaskData.json')
    clean_parse(read_path, write_path)