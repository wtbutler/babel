from hexTiles.Hexagon import Hexagon

class StraightHallway(Hexagon):
    def __init__(self, orientation):
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
