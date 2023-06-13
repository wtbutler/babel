# Types of openings:
#       U, SU, D, SD, N, NE, SE, S, SW, NW
#           (Includes Stairs Up and Stairs Down as connection types)
# Directions:
#       U, D, N, NE, SE, S, SW, NW
# Categories:
#       Hall, Shelf, Circle, Void
# Barriers:
#       Wall, Gap, Stairs, Walkway, Corridor

class Hexagon:
    def super(self):
        self.neighbor_options = {"U": set(), "D": set(), "N": set(), "NE": set(), "SE": set(), "S": set(), "SW": set(), "NW": set()}
        self.barrier_options = {"U": set(), "D": set(), "N": set(), "NE": set(), "SE": set(), "S": set(), "SW": set(), "NW": set()}
        self.weight = 1
        # self.tags = set()
        # self.initTags()

    def addTags(self, tags):
        self.tags = self.tags.union(tags)
        return self

    def initTags(self):
        self.tags = set()
        for i in self.openings:
            self.tags.add("Opening " + i)
        print(self.tags)

    def getNeighborOptions(self):
        return {d: self.neighbor_options[d].copy() for d in self.neighbor_options}

    def requirements(self, barriers):
        return barriers

    def __str__(self):
        name = type(self).__name__
        if name == "Circle" or name == "Void":
            return f"<{type(self).__name__}>"
        return f"<{type(self).__name__} facing {self.orientation}>"
    def __repr__(self):
        name = type(self).__name__
        if name == "Circle" or name == "Void":
            return f"<{type(self).__name__}>"# at {hex(id(self))}>"
        return f"<{type(self).__name__} with orientation {self.orientation}>"# at {hex(id(self))}>"
