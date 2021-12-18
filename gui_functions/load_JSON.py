import json


def main(file_path):
    f = open(file_path)
    data_contents = json.load(f)
    f.close()

    return data_contents
