from hexTiles.Hallway import Hallway

class WheelHallway(Hallway):
    def __init__(self, orientation):
        self.super()
        if orientation == "S" or orientation == "NW" or orientation == "NE":
            self.sprite = (1, 1)
            self.orientation = "S"
            self.openings = {"S", "NW", "NE"}
        elif orientation == "N" or orientation == "SE" or orientation == "SW":
            self.sprite = (1, 2)
            self.orientation = "N"
            self.openings = {"N", "SE", "SW"}
        else:
            raise WrongOrientationError
        self.barrier_options["U"].add("Stairs")
        self.barrier_options["D"].add("Stairs")
        for opening, s in self.barrier_options.items():
            if opening in self.openings:
                self.barrier_options[opening].add("Corridor")
            else:
                self.barrier_options[opening].add("Wall")
        self.openings.add("U")
        self.openings.add("D")
        self.category = "Hall"
