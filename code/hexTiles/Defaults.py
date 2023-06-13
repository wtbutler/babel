from hexTiles import WheelHallway, StraightHallway, BentHallway
from hexTiles import Circle, Void
from hexTiles import Bookshelf, Nook

class Defaults:
    # TODO: make an elbow hex
    Wheel_N = WheelHallway.WheelHallway("N")
    Wheel_S = WheelHallway.WheelHallway("S")

    Straight_N  = StraightHallway.StraightHallway("N")
    Straight_NE = StraightHallway.StraightHallway("NE")
    Straight_SE = StraightHallway.StraightHallway("SE")

    Bent_N  = BentHallway.BentHallway("N")
    Bent_NE = BentHallway.BentHallway("NE")
    Bent_SE = BentHallway.BentHallway("SE")
    Bent_S  = BentHallway.BentHallway("S")
    Bent_SW = BentHallway.BentHallway("SW")
    Bent_NW = BentHallway.BentHallway("NW")

    Circle = Circle.Circle()
    Void = Void.Void()

    Shelf_N  = Bookshelf.Bookshelf("N")
    Shelf_NE = Bookshelf.Bookshelf("NE")
    Shelf_SE = Bookshelf.Bookshelf("SE")
    Shelf_S  = Bookshelf.Bookshelf("S")
    Shelf_SW = Bookshelf.Bookshelf("SW")
    Shelf_NW = Bookshelf.Bookshelf("NW")

    Nook_N  = Nook.Nook("N")
    Nook_NE = Nook.Nook("NE")
    Nook_SE = Nook.Nook("SE")
    Nook_S  = Nook.Nook("S")
    Nook_SW = Nook.Nook("SW")
    Nook_NW = Nook.Nook("NW")

    all_prototypes = {Wheel_N, Wheel_S,
                Straight_N, Straight_NE, Straight_SE,
                Bent_N, Bent_NE, Bent_SE, Bent_S, Bent_SW, Bent_NW,
                Circle, Void,
                Shelf_N, Shelf_NE, Shelf_SE, Shelf_S, Shelf_SW, Shelf_NW,
                Nook_N, Nook_NE, Nook_SE, Nook_S, Nook_SW, Nook_NW
              }

    directions = {"U", "D", "N", "NE", "SE", "S", "SW", "NW"}

    links = {   "U":"D",
                "D":"U",
                "N":"S",
                "NE":"SW",
                "SE":"NW",
                "S":"N",
                "SW":"NE",
                "NW":"SE"}

    barriers = {"Wall", "Gap", "Stairs", "Corridor", "Walkway"}

    for hexTile in all_prototypes:
        for consider in all_prototypes:
            for direct in directions:
                aBarriers = hexTile.barrier_options[direct]
                bBarriers = consider.barrier_options[links[direct]]
                overlap = aBarriers.intersection(bBarriers)
                if overlap:
                    hexTile.neighbor_options[direct].add(consider)
