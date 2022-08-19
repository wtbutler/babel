from hexTiles.Hexagon import Hexagon

class Circle(Hexagon):
    def __init__(self):
        self.sprite = (0, 2)
        self.orientation = "N"
        self.openings = {"D", "N", "NE", "SE", "S", "SW", "NW", "U"}
        self.super()
        for opening in self.openings:
            self.barrier_options[opening].add("Gap")
        self.barrier_options["U"].add("Wall")
        self.category = "Circle"

    def requirements(self):
        # Must have at least one stairway connection
        return
