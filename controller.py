# logic.py
import json
from die import Die
from host_interface import HostInterface


class DataManager:
    def __init__(self, filename):
        print(filename)
        self.filename = filename
        self.die_objects = {}

    def load_die(self, die_index):
        if die_index not in self.die_objects:
            with open(self.filename, 'r') as config:
                data = json.load(config)
            die_json = data.get("Top",[]).get("DIES", [])[die_index]
            self.die_objects[die_index] = Die(die_index, die_json)
        return self.die_objects[die_index]

    def get_total_dies(self):
        with open(self.filename, 'r') as config:
            data = json.load(config)
        return len(data.get("Top",[]).get("DIES", []))

    def load_host_interface(self):
        with open(self.filename, 'r') as config:
            data = json.load(config)
        host_interface_data = data.get("Top", {}).get("Host_interface", {})
        self.host_interface = HostInterface(host_interface_data)
        print("g2h",self.host_interface.g2h)
        return self.host_interface
