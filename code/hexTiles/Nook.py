from hexTiles.Hexagon import Hexagon

class Nook(Hexagon):
    def __init__(self, orientation):
        self.super()
        order = ["N", "NE", "SE", "S", "SW", "NW"]
        if orientation in order:
            self.sprite = (4, order.index(orientation))
            self.orientation = orientation
            self.openings = {orientation}
        else:
            raise WrongOrientationError
        self.weight = 0.1
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
