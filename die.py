from cluster import Cluster
from component import Component
from quad import Quad
from constants import QUAD


class Die(Component):
    def __init__(self, id, data):
        super().__init__(id, 'DIE')
        self.quads = [[None for _ in range(2)] for _ in range(2)]
        self.data = data
        self.init_quads()

    def init_quads(self):

        quads = self.data.get("GRID", {}).get("QUADS", [])

        positions = [(0, 0), (0, 1), (1, 0), (1, 1)]

        for index, quad_data in enumerate(quads):
            pos = positions[index % len(positions)]
            row, col = pos

            new_quad = Quad(quad_data.get("id"), quad_data.get("name"),quad_data)


            self.quads[row][col] = new_quad


    def print_quads(self):
        for row in range(len(self.quads)):
            for col in range(len(self.quads[row])):
                quad = self.quads[row][col]
                if quad is None:
                    print("Empty", end="\t")
                else:
                    clusters_info = " | ".join(f"{c.cluster_id}:{c.type_name}" for c in quad.clusters)
                    print(f"({quad.id}) {clusters_info}", end="\t")
            print()  # Newline after each row