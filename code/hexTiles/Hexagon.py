
class Hexagon:
    def __init__(self, pos):
        self.sprite = (0, 0)
        self.openings = {"N", "NE", "S", "SW"}
        self.orientation = "N"
        self.optional_openings = {"U"}
