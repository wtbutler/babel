from hexTiles.Hexagon import Hexagon

class Void(Hexagon):
    def __init__(self):
        self.sprite = (0, 1)
        self.orientation = "N"
        self.openings = set()
        self.category = "Void"
        self.super()

    def requirements(self):
        # Must have at least one stairway connection
        return
