import json
from gui_functions.load_JSON import main as load_json


def main(file_path, remove_key):
    json_dict = load_json(file_path)
    json_dict.pop(remove_key)

    f = open(file_path, 'w')
    json.dump(json_dict, f, indent=4)
    f.close()
