from cluster import Cluster
from component import Component
from constants import *

class Ecore(Cluster):
    def __init__(self,cluster, data):
        row, col, cluster_id, size_pixels, color, type_name=cluster
        super().__init__(row, col, cluster_id, size_pixels, color, type_name)
        self.data = data
        self.ecores = data[ECORES]
        self.bmt=Component(-1,data.get('BMT', {}))  # Set to empty dict if no data
        self.cbus_inj= Component(-1, data[CBUS_INJ])
        self.cbus_clt=Component(-1, data[CBUS_CLT])
        self.nfi_inj=Component(-1,data[NFI_INJ])
        self.nfi_clt=Component(-1,data[NFI_CLT])
