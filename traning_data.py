from flask import json
import datetime
import glob


def save_to_file(data):
    try:
        now = datetime.datetime.now()
        with open('training_data/' + str(data['expected-prediction']) + '/' + str(now) + '.json', 'w') as outfile:
            json.dump(data, outfile)

        return True
    except Exception:
        return False


def upload_training_data(path, number=0):
    training_array = []
    files = glob.glob(path + number + "/*.json")
    for file in files:
        print(str(file))
        with open(str(file)) as json_file:
            data = json.load(json_file)
            training_array.append(data)

    return training_array

