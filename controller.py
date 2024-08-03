# logic.py
import json
from die import Die

class DataManager:
    def __init__(self, filename):
        print(filename)
        self.filename = filename
        self.die_objects = {}

    def load_die(self, die_index):
        if die_index not in self.die_objects:
            with open(self.filename, 'r') as config:
                data = json.load(config)
            die_json = data.get("DIES", [])[die_index]
            self.die_objects[die_index] = Die(die_index, die_json)
        return self.die_objects[die_index]

    def get_total_dies(self):
        with open(self.filename, 'r') as config:
            data = json.load(config)
        return len(data.get("DIES", []))
