from hexTiles.Hexagon import Hexagon

class Bookshelf(Hexagon):
    def __init__(self, orientation):
        self.super()
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
        self.weight = 2
        for opening, s in self.barrier_options.items():
            if opening in self.openings:
                self.barrier_options[opening].add("Walkway")
                self.barrier_options[opening].add("Corridor")
            else:
                self.barrier_options[opening].add("Wall")
        self.openings.add("U")
        self.barrier_options["U"].add("Wall")
        self.barrier_options["U"].add("Gap")
        self.barrier_options["D"].add("Wall")
        self.category = "Shelf"

    def requirements(self, barriers):
        # Must have at least one Corridor connection
        passes = 0
        for d in barriers:
            if "Corridor" in barriers[d]:
                passes += 1
        if not passes:
            return None
        if passes > 1:
            return barriers
        for d in barriers:
            if "Corridor" in barriers[d]:
                if len(barriers[d]) != 1:
                    print("Collapsing due to requirements")
                    print(barriers[d])
                barriers[d] = barriers[d].intersection({"Corridor"})
        return barriers
