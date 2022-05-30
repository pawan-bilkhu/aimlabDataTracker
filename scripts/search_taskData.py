import settings
import json


def search_taskData(file_path, date, task, field, mode):

    with open(file_path, 'r') as file:
        data = json.load(file)
    taskData = []
    count = 0
    for entry in data:
        if mode != 0:
            if task in entry[field] and date in entry["create_date"] and mode == entry["mode"]:
                count = count + 1
                print(entry)
                taskData.append(entry)
        elif task in entry[field] and date in entry["create_date"]:
            count = count + 1
            print(entry)
            taskData.append(entry)
    print(f'Returned {count} results.')
    # return taskData


if __name__ == '__main__':
    path = settings.joinpath(settings.DATA, 'cleanData/cleanTaskData.json')
    task = "startrack"
    for i in range(1, 32):
        date = "2021-12-"
        if i < 10:
            date = date + "0" + str(i)
        else:
            date = date + str(i)
        print(f'---Date: {date}---')
        search_taskData(path, date, task, "taskName", 0)
