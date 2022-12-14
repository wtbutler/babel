from hexTiles import WheelHallway, StraightHallway, BentHallway
from hexTiles import Circle, Void
from hexTiles import Bookshelf

class Defaults:
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

    options = {Wheel_N, Wheel_S,
                Straight_N, Straight_NE, Straight_SE,
                Bent_N, Bent_NE, Bent_SE, Bent_S, Bent_SW, Bent_NW,
                Circle, Void,
                Shelf_N, Shelf_NE, Shelf_SE, Shelf_S, Shelf_SW, Shelf_NW
              }

    categories = {"Hall", "Shelf", "Circle", "Void"}
    directions = {"U", "D", "N", "NE", "SE", "S", "SW", "NW"}

    links = {   "U":"D",
                "D":"U",
                "N":"S",
                "NE":"SW",
                "SE":"NW",
                "S":"N",
                "SW":"NE",
                "NW":"SE"}

    for hexTile in options:
        for option in hexTile.options:
            pass

    for hexTile in options:
        for consider in options:
            for direct in directions:
                aBarriers = hexTile.barrier_options[direct]
                bBarriers = consider.barrier_options[links[direct]]
                overlap = aBarriers.intersection(bBarriers)
                if overlap:
                    hexTile.options[direct].add(consider)
