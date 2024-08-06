# logic.py
import json
from die import Die
from host_interface import HostInterface


class DataManager:
    def __init__(self, chip_file,sl_file):
        self.chip_file = chip_file
        self.sl_file = sl_file
        with open(self.sl_file, 'r') as config:
            self.sl_data = json.load(config)
        self.die_objects = {}

    def load_die(self, die_index):

        if die_index not in self.die_objects:
            with open(self.chip_file, 'r') as config:
                data = json.load(config)
            die_json = data.get("Top",[]).get("DIES", [])[die_index]
            self.die_objects[die_index] = Die(die_json['id'], die_json)
            if(len(self.die_objects)==2):
                self.enable_widgets()

        return self.die_objects[die_index]

    def get_total_dies(self):
        with open(self.chip_file, 'r') as config:
            data = json.load(config)
        return len(data.get("Top",[]).get("DIES", []))

    def load_host_interface(self):
        with open(self.chip_file, 'r') as config:
            data = json.load(config)
        host_interface_data = data.get("Top", {}).get("Host_interface", {})
        print(host_interface_data)  # For debugging
        self.host_interface = HostInterface(host_interface_data)
        return self.host_interface

    def enable_widget_by_id(self,id):
        col,did,quad,row=id["col"],id["did"],id["quad"],id["row"]
        current_quad = self.die_objects[did].quads[quad // 2][quad % 2]
        current_quad.clusters[row][col].is_enable = True
        current_quad.is_enable = True

    def enable_die(self):
        for die_id, die in self.die_objects.items():
            for row in die.quads:
                for quad in row:
                    if quad and quad.is_enable:
                        die.is_enable = True
                        break  # Exit inner loop if any quad is enabled
                if die.is_enable:
                    break  # Exit outer loop if die is enabled

    def enable_widgets(self):
        for id in self.sl_data["enabled_clusters"]:
            self.enable_widget_by_id(id['id'])
        print(self.die_objects)
        self.enable_die()



