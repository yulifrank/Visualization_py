from component import Component

class Cluster(Component):
    def __init__(self, row, col, cluster_id, size_pixels, color ,type_name):
        super().__init__(cluster_id, type_name)
        self.row = row
        self.col = col
        self.size_pixels = size_pixels
        self.color = color
        self.is_enable = False


    def __str__(self):
        return f"{self.row,self.col}{self.type_name}"

