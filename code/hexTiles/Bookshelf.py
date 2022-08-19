from hexTiles.Hexagon import Hexagon

class Bookshelf(Hexagon):
    def __init__(self, orientation):
        if orientation == "N":
            self.sprite = (3, 0)
            self.orientation = "N"
            self.openings = {"NW", "NE"}
        elif orientation == "NE":
            self.sprite = (3, 1)
            self.orientation = "NE"
            self.openings = {"N", "SE"}
        elif orientation == "SE":
            self.sprite = (3, 2)
            self.orientation = "SE"
            self.openings = {"NE", "S"}
        elif orientation == "S":
            self.sprite = (3, 3)
            self.orientation = "S"
            self.openings = {"SE", "SW"}
        elif orientation == "SW":
            self.sprite = (3, 4)
            self.orientation = "SW"
            self.openings = {"S", "NW"}
        elif orientation == "NW":
            self.sprite = (3, 5)
            self.orientation = "NW"
            self.openings = {"SW", "N"}
        else:
            raise WrongOrientationError
        self.openings.add("U")
        self.category = "Shelf"
        self.super()

    def requirements(self):
        # Must have at least one stairway connection
        return
