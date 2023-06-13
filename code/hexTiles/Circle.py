from hexTiles.Hexagon import Hexagon

class Circle(Hexagon):
    def __init__(self):
        self.super()
        self.sprite = (1, 0)
        self.orientation = "N"
        self.openings = {"N", "NE", "SE", "S", "SW", "NW"}
        self.weight = 0.1
        for opening in self.openings:
            self.barrier_options[opening].add("Walkway")
            self.barrier_options[opening].add("Corridor")
        self.openings.add("U")
        self.barrier_options["U"].add("Wall")
        self.barrier_options["U"].add("Gap")
        self.openings.add("D")
        self.barrier_options["D"].add("Gap")
        self.category = "Circle"

    def requirements(self, barriers):
        # Must have at least one Walkway or Corridor connection
        passes = 0
        for d in barriers:
            if "Corridor" in barriers[d] or "Walkway" in barriers[d]:
                passes += 1
        if not passes:
            return None
        if passes > 1:
            return barriers
        for d in barriers:
            if "Corridor" in barriers[d] or "Walkway" in barriers[d]:
                if len(barriers[d]) != 1:
                    print("Collapsing due to requirements")
                    print(barriers[d])
                barriers[d] = barriers[d].intersection({"Corridor", "Walkway"})
        return barriers
