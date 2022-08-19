from hexTiles.Defaults import Defaults as D
import pygame
tile_size = X, Y = 26, 22

class T:
    def __init__(self, pos, shape=None):
        self.pos = pos
        self.neighbors = {}
        self.options = D.options.copy()
        self.shape = shape

class HexSheet:
    def draw_sheet(self, screen):
        #screen.blit(self.hexx, (0, 0))
        #return
        #for j, row in enumerate(self.sheet):
            #for tile in row:
            #for i, t in enumerate(row):
        for (i, j), t in self.sheet.items():
            if not self.drawn: print(t.shape)
            y, x = t.shape.sprite
            screen.blit(self.tiles[y][x], (i*(X-6), j*Y + i*(Y/2)))
        self.drawn = True

    def getNeighborCoords(self, coords):
        x, y = coords
        return {(x-1, y), (x-1, y-1), (x, y-1), (x+1, y), (x+1, y+1), (x, y+1)}
    
    def addTileToSheet(self, pos, tileType):
        new = T(pos, tileType)
        self.sheet[pos] = new
        neighborCoords = self.getNeighborCoords(pos)
        print(neighborCoords)
        for neighbor in neighborCoords:
            if neighbor in self.sheet:
                new.neighbors.add(neighbor)
                self.sheet[neighbor].neighbors.add(new)

    def __init__(self, tilesheet):
        self.drawn = False
        self.hexx = tilesheet.convert_alpha()
        self.hexrect = self.hexx.get_rect()
        if False:
            self.sheet = [  
                            [T(D.Straight_SE), T(D.Circle), T(D.Shelf_N), T(D.Shelf_SE)],
                            [T(D.Shelf_N),  T(D.Wheel_N), T(D.Circle), T(D.Shelf_NW)],
                            [T(D.Shelf_SE), T(D.Shelf_S), T(D.Bent_N), T(D.Void)],
                            [T(D.Circle), T(D.Shelf_SW), T(D.Void), T(D.Void)]
                        ]
        self.sheet = {}
        self.frontier = set()
        self.addTileToSheet((0, 0), D.Circle)
        self.tiles = []
        for j in range(4):
            tmp = []
            for i in range(6):
                t = pygame.Surface((X, Y)).convert_alpha()
                t.fill((0, 0, 0, 0))
                t.blit(self.hexx, (0, 0), (X * i, Y * j, X, Y))
                tmp += [t]
            self.tiles += [tmp]
