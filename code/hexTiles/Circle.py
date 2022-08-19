from hexTiles.Hexagon import Hexagon

class Circle(Hexagon):
    def __init__(self):
        self.sprite = (0, 2)
        self.orientation = "N"
        self.openings = {"D", "N", "NE", "SE", "S", "SW", "NW", "U"}
        self.category = "Circle"
        self.super()

    def requirements(self):
        # Must have at least one stairway connection
        return
