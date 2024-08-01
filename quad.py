from component import Component
from constants import *
from cluster import Cluster
class Quad(Component):
    def __init__(self, id, name,data):
        super().__init__(id, QUAD)
        self.name = name
        self.data =data
        self.clusters = [[None for _ in range(8)] for _ in range(8)]

        self.init_clusters()

    def init_clusters(self):
        self.init_ecore()
        self.init_cbus()
        self.init_tcus()

    def init_ecore(self):
        ecore = self.data["Ecore"]
        self.init_cluster(ecore,ECORE)


    def init_cbus(self):
        cbus = self.data.get("CBUs", [])
        for cbu in cbus:
            if not isinstance(cbu, dict):
                print(f"Warning: Invalid CBU data: {cbu}")
                continue
            self.init_cluster(cbu,CBU)


    def init_tcus(self):
        tcus = self.data.get("TCUs", [])
        for tcu in tcus:
            if not isinstance(tcu, dict):
                print(f"Warning: Invalid TCU data: {tcu}")
                continue
            self.init_cluster(tcu,TCU)



    def init_cluster(self,cluster_json,type):
        cluster = Cluster(
            row=cluster_json.get("row"),
            col=cluster_json.get("col"),
            cluster_id=cluster_json.get("cluster_id"),
            size_pixels= 2,
            color=CLASTER_COLORS[type],
            type_name=type
        )
        self.clusters[cluster.row][cluster.col]=cluster

    def __str__(self):
        return f"Quad(id={self.id})"