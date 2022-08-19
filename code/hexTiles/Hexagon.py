# Types of openings:
#       U, SU, D, SD, N, NE, SE, S, SW, NW
#           (Includes Stairs Up and Stairs Down as connection types)
# Directions:
#       U, D, N, NE, SE, S, SW, NW
# Categories:
#       Hall, Shelf, Circle, Void

class Hexagon:
    def super(self):
        self.options = {"U": set(), "D": set(), "N": set(), "NE": set(), "SE": set(), "S": set(), "SW": set(), "NW": set()}
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

    def __str__(self):
        return f"<{type(self).__name__} with orientation {self.orientation}>"
