import json

class JSONHandler:
    def __init__(self):
        pass

    def load(self, path):
        pass

    def json_to_dict(self, file) -> dict:
        return json.loads(file)

    def merge_dicts(self, d1, d2):
        for key, value in d2.items():
            if key in d1:
                print("Key found in both dictionaries. Merging values.")
            else:
                d1[key] = value