from hexTiles.Hexagon import Hexagon

class WheelHallway(Hexagon):
    def __init__(self, orientation):
        if orientation == "S" or orientation == "NW" or orientation == "NE":
            self.sprite = (0, 3)
            self.orientation = "S"
            self.openings = {"S", "NW", "NE"}
        elif orientation == "N" or orientation == "SE" or orientation == "SW":
            self.sprite = (0, 4)
            self.orientation = "N"
            self.openings = {"N", "SE", "SW"}
        else:
            raise WrongOrientationError
        self.openings.add("U")
        self.openings.add("D")
        self.category = "Hall"
        self.super()

    def requirements(self):
        # Must have at least one stairway connection
        return
