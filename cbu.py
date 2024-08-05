from cluster import Cluster


class Cbu(Cluster):
    def __init__(self,cluster,data):
        row, col, cluster_id, size_pixels, color, type_name=cluster
        super().__init__(row, col, cluster_id, size_pixels, color ,type_name)
        self.data=data