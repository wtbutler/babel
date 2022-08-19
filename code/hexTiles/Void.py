from hexTiles.Hexagon import Hexagon

class Void(Hexagon):
    def __init__(self):
        self.sprite = (0, 1)
        self.orientation = "N"
        self.openings = {}

    def requirements(self):
        # Must have at least one stairway connection
        return
