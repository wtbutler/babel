from hexTiles.Hexagon import Hexagon

class StraightHallway(Hexagon):
    def __init__(self, orientation):
        self.optional_openings = {"U", "D"}
        if orientation == "N" or orientation == "S":
            self.sprite = (1, 0)
            self.orientation = "N"
            self.openings = {"N", "S"}
        elif orientation == "NE" or orientation == "SW":
            self.sprite = (1, 1)
            self.orientation = "NE"
            self.openings = {"NE", "SW"}
        elif orientation == "SE" or orientation == "NW":
            self.sprite = (1, 2)
            self.orientation = "SE"
            self.openings = {"SE", "NW"}
        else:
            raise WrongOrientationError

    def requirements(self):
        # Must have at least one stairway connection
        return
