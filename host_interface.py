# host_interface.py

from component import Component

class HostInterface(Component):
    def __init__(self, data):
        super().__init__(-1, "host_interface")
        self.bmt = data.get('BMT', 'Unknown')
        self.h2g = data.get('H2G', {})
        self.g2h = data.get('G2H', {}).get('EQs', [])
        # Add more attributes as needed based on the JSON structure

    def get_bmt(self):
        print("get_bmt")
        return self.bmt

    def get_h2g(self):
        print("get_h2g")

        return self.h2g

    def get_g2h(self):
        return self.g2h

    def __str__(self):
        return f"HostInterface(BMT={self.bmt}, H2G={self.h2g}, G2H={self.g2h})"
