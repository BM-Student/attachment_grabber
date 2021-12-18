import json
from gui_functions.load_JSON import main as load_json
import re


def main(file_path, dict_ob):
    json_dict = load_json(file_path)
    dict_ob = handle_dupe_key(json_dict, dict_ob)
    json_dict.update(dict_ob)

    f = open(file_path, 'w')
    json.dump(json_dict, f, indent=4)
    f.close()


def handle_dupe_key(json_dict, dict_ob):
    di_check = lambda x: f'{x.split(" |Flags: ")[0]} di' if ' di' in x else x.split(" |Flags: ")[0]
    dict_ob_path = list(dict_ob.keys())[0].split(" |Flags: ")[0]
    if len(list(dict_ob.keys())[0].split(" |Flags: ")) > 1:
        dict_ob_flags = list(dict_ob.keys())[0].split(" |Flags: ")[-1]
    else:
        dict_ob_flags = ''
    paths = [di_check(x) for x in json_dict.keys()]
    if dict_ob_path in paths:
        count = find_count(list(json_dict.keys()), dict_ob_path)
        count_flag = f'c{count}'
        dict_ob_path = f'{dict_ob_path} |Flags: {dict_ob_flags}'
        if dict_ob_path[-1] == " ":
            dict_ob_path = f'{dict_ob_path}{count_flag}'
        else:
            dict_ob_path = f'{dict_ob_path}, {count_flag}'
    else:
        dict_ob_path = f'{dict_ob_path} |Flags: {dict_ob_flags}'
        if dict_ob_path[-1] == " ":
            dict_ob_path = f'{dict_ob_path}c0'
        else:
            dict_ob_path = f'{dict_ob_path}, c0'
    new_dict = {str(dict_ob_path): dict_ob[list(dict_ob.keys())[0]]}

    return new_dict


def find_count(paths_raw, dict_ob_path):
    dupe_paths = [x for x in paths_raw if dict_ob_path in x]
    if len(dupe_paths) == 0:
        return 0
    else:
        numbers = sorted([int(re.search('c[0-9]+', x).group().replace('c', '')) for x in dupe_paths if re.search('c[0-9]+', x)], reverse=True)
        return numbers[0] + 1



