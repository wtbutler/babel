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
