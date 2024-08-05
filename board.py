

class Board:
    def __init__(self, size_mm, size_pixels, color):
        self.width_mm = size_mm['width_mm']
        self.height_mm = size_mm['height_mm']
        self.size_pixels = size_pixels
        self.color = color
        self.dies = []

    def add_die(self, die):
        self.dies.append(die)