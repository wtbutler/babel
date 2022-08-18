import pygame
tile_size = X, Y = 26, 22

class Hexagon:
    def __init__(self, pos):
        self.pos = pos
        self.sprite = (0, 0)
        self.openings = {"N", "NE", "S", "SW"}
        self.orientation = "N"
        self.neighbors = {}
        self.optional_openings = {"U"}
    CIRCLE = (0, 2)
    BLANK = (0, 1)
    HS_N = (1, 0)
    HS_NE = (1, 1)
    HS_SE = (1, 2)
    HB_N = (2, 0)
    HB_NE = (2, 1)
    HB_SE = (2, 2)
    HB_S = (2, 3)
    HB_SW = (2, 4)
    HB_NW = (2, 5)
    HW_N = (0, 3)
    HW_S = (0, 4)
    B_N = (3, 0)
    B_NE = (3, 1)
    B_SE = (3, 2)
    B_S = (3, 3)
    B_SW = (3, 4)
    B_NW = (3, 5)

class StraightHallway(Hexagon):
    def __init__(self, pos, orientation):
        self.pos = pos
        self.optional_openings = {"U", "D"}
        if orientation == "N" or orientation == "S":
            self.sprite = (1, 0)
            self.orientation = "N"
            self.openings = {"N", "S"}
        elif orientation == "NE" or orientation == "SW":
            self.sprite = (1, 1)
            self.orientation = "NE"
            self.openings = {"NE", "SW"}
        elif orientation == "SE" or orientation == "NW":
            self.sprite = (1, 2)
            self.orientation = "SE"
            self.openings = {"SE", "NW"}
        else:
            raise WrongOrientationError

    def requirements(self):
        # Must have at least one stairway connection
        return

class HexSheet:
    def draw_sheet(self, screen):
        #screen.blit(self.hexx, (0, 0))
        #return
        for j, row in enumerate(self.sheet):
            #for tile in row:
            for i, (y, x) in enumerate(row):
                screen.blit(self.tiles[y][x], (i*(X-6), j*Y + i*(Y/2)))

    def __init__(self, tilesheet):
        self.hexx = tilesheet.convert_alpha()
        self.hexrect = self.hexx.get_rect()
        self.sheet = [  
                        [T.HS_SE, T.CIRCLE, T.B_N, T.B_SE],
                        [T.B_N,  T.HW_S, T.CIRCLE, T.B_NW],
                        [T.B_SE, T.B_S, T.HB_N, T.BLANK],
                        [T.CIRCLE, T.B_SW, T.BLANK, T.BLANK]
                    ]
        self.tiles = []
        for j in range(4):
            tmp = []
            for i in range(6):
                t = pygame.Surface((X, Y)).convert_alpha()
                t.fill((0, 0, 0, 0))
                t.blit(self.hexx, (0, 0), (X * i, Y * j, X, Y))
                tmp += [t]
            self.tiles += [tmp]
