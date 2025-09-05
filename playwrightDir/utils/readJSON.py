import json
import os


def read_json(file_name, key):
    base_path = os.path.dirname(__file__)  # current file's dir
    file_path = os.path.join(base_path, '../data', file_name)
    file_path = os.path.abspath(file_path)
    with open(file_path, 'r') as data:
        content = json.load(data)
        print(content)
        return content[key]
