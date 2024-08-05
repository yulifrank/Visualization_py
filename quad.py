from component import Component
from constants import *
from cluster import Cluster
from ecore import Ecore
from cbu import Cbu
from tcu import Tcu

class Quad(Component):
    def __init__(self, id, name, data):
        super().__init__(id, QUAD)
        self.name = name
        self.data = data
        self.clusters = [[None for _ in range(8)] for _ in range(8)]

        self.init_clusters()

    def init_clusters(self):
        self.init_ecore()
        self.init_cbus()
        self.init_tcus()

    def init_ecore(self):
        ecore_json = self.data["Ecore"]
        cluster=self.init_cluster(ecore_json, ECORE)
        ecore=Ecore(cluster,ecore_json)
        self.clusters[int(ecore.row)][int(ecore.col)] = ecore

    def init_cbus(self):
        cbus = self.data.get("CBUs", [])
        for cbu_json in cbus:
            if not isinstance(cbu_json, dict):
                print(f"Warning: Invalid CBU data: {cbu_json}")
                continue
            cluster=self.init_cluster(cbu_json, CBU)
            cbu = Cbu(cluster, cbu_json)
            self.clusters[int(cbu.row)][int(cbu.col)] = cbu


    def init_tcus(self):
        tcus = self.data.get("TCUs", [])
        for tcu_json in tcus:
            if not isinstance(tcu_json, dict):
                print(f"Warning: Invalid TCU data: {tcu_json}")
                continue
            cluster=self.init_cluster(tcu_json, TCU)
            tcu = Tcu(cluster, tcu_json)
            self.clusters[int(tcu.row)][int(tcu.col)] = tcu

    def init_cluster(self, cluster_json, type):
        cluster = [cluster_json.get("row"),
                   cluster_json.get("col"),
                   cluster_json.get("cluster_id"),
                   2,
                   CLASTER_COLORS[type],
                   type]
        return cluster
       # self.clusters[cluster.row][cluster.col] = cluster

    def __str__(self):
        return f"Quad(id={self.id})"
