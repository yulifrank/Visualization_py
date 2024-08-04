from component import Component

class HostInterface(Component):
    def __init__(self, data):
        super().__init__(-1, "host_interface")
        self.bmt = Component(-1, data.get('BMT', {}))  # Set to empty dict if no data
        self.h2g = {k: Component(-1, v) for k, v in data.get('H2G', {}).items()}
        self.g2h = [Component(eq['id'], eq['event_queue']) for eq in data.get('G2H', {}).get('EQs', [])]
        self.g2h.append(Component(-1, data.get('G2H', {}).get('g2h_IRQA', {})))  # Set to empty dict if no data
        self.pcie = Component(-1, data.get('PCIe', {}))  # Set to empty dict if no data

    def get_bmt(self):
        return self.bmt if self.bmt.type_name != 'Unknown' else None

    def get_h2g(self):
        return self.h2g

    def get_g2h(self):
        return self.g2h

    def get_pcie(self):
        return self.pcie if self.pcie.type_name != 'Unknown' else None

    def __str__(self):
        return f"HostInterface(BMT={self.bmt}, H2G={self.h2g}, G2H={self.g2h}, PCIe={self.pcie})"
