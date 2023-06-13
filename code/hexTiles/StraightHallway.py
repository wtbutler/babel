from hexTiles.Hallway import Hallway

class StraightHallway(Hallway):
    def __init__(self, orientation):
        self.super()
        if orientation == "N" or orientation == "S":
            self.sprite = (1, 3)
            self.orientation = "N"
            self.openings = {"N", "S"}
        elif orientation == "NE" or orientation == "SW":
            self.sprite = (1, 4)
            self.orientation = "NE"
            self.openings = {"NE", "SW"}
        elif orientation == "SE" or orientation == "NW":
            self.sprite = (1, 5)
            self.orientation = "SE"
            self.openings = {"SE", "NW"}
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
