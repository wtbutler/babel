from hexTiles.Hexagon import Hexagon

class Void(Hexagon):
    def __init__(self):
        self.sprite = (0, 1)
        self.orientation = "N"
        self.openings = set()
        self.super()
        for opening, s in self.barrier_options.items():
            self.barrier_options[opening].add("Wall")
        self.category = "Void"

    def requirements(self):
        # Must have at least one stairway connection
        return
