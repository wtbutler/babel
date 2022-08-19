from hexTiles.Hexagon import Hexagon

class Circle(Hexagon):
    def __init__(self):
        self.sprite = (0, 2)
        self.orientation = "N"
        self.openings = {"D"}
        self.optional_openings = {"N", "NE", "SE", "S", "SW", "NW"}

    def requirements(self):
        # Must have at least one stairway connection
        return
