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
        self.super()
        self.barrier_options["U"].add("Stairs")
        self.barrier_options["D"].add("Stairs")
        for opening, s in self.barrier_options.items():
            if opening in self.openings:
                self.barrier_options[opening].add("Gap")
            else:
                self.barrier_options[opening].add("Wall")
        self.openings.add("U")
        self.openings.add("D")
        self.category = "Hall"

    def requirements(self):
        # Must have at least one stairway connection
        return
