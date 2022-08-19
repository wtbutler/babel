from hexTiles.Hexagon import Hexagon

class BentHallway(Hexagon):
    def __init__(self, orientation):
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
