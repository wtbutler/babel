from hexTiles.Hexagon import Hexagon

class Void(Hexagon):
    def __init__(self):
        self.super()
        self.sprite = (0, 2)
        self.orientation = "N"
        self.openings = set()
        for d, s in self.barrier_options.items():
            s.add("Wall")
        self.category = "Void"
