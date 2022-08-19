from hexTiles.Hexagon import Hexagon

class BentHallway(Hexagon):
    def __init__(self, orientation):
        self.optional_openings = {"U", "D"}
        if orientation == "N":
            self.sprite = (2, 0)
            self.orientation = "N"
            self.openings = {"NW", "NE"}
        elif orientation == "NE":
            self.sprite = (2, 1)
            self.orientation = "NE"
            self.openings = {"N", "SE"}
        elif orientation == "SE":
            self.sprite = (2, 2)
            self.orientation = "SE"
            self.openings = {"NE", "S"}
        elif orientation == "S":
            self.sprite = (2, 3)
            self.orientation = "S"
            self.openings = {"SE", "SW"}
        elif orientation == "SW":
            self.sprite = (2, 4)
            self.orientation = "SW"
            self.openings = {"S", "NW"}
        elif orientation == "NW":
            self.sprite = (2, 5)
            self.orientation = "NW"
            self.openings = {"SW", "N"}
        else:
            raise WrongOrientationError

    def requirements(self):
        # Must have at least one stairway connection
        return
