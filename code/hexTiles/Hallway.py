from hexTiles.Hexagon import Hexagon

class Hallway(Hexagon):
    def requirements(self, barriers):
        # Must have at least one Stairs connection
        passes = 0
        for d in barriers:
            if "Stairs" in barriers[d]:
                passes += 1
        if not passes:
            return None
        if passes > 1:
            return barriers
        for d in barriers:
            if "Stairs" in barriers[d]:
                if len(barriers[d]) != 1:
                    print("Collapsing due to requirements")
                    print(barriers[d])
                barriers[d] = barriers[d].intersection({"Stairs"})
        return barriers
