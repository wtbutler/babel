from hexTiles.Defaults import Defaults as D
from hexTiles.Nook import Nook
import pygame
import random
tile_size = X, Y = 26, 22

# (important) -> (neighbor)
def getDirectionFromRelativeCoords(c, c1):
    x, y = c
    x1, y1 = c1
    if y1 > y:
        if x1 > x:
            return "NE"
        return "N"
    elif y1 < y:
        if x1 < x:
            return "SW"
        return "S"
    if x1 > x:
        return "SE"
    return "NW"

def hex_manhatten(p0, p1):
    x0, y0 = p0
    x1, y1 = p1
    dx = x1 - x0
    dy = y1 - y0
    if (dx>0) == (dy>0):
        return max(abs(dx), abs(dy))
    return abs(dx)+abs(dy)
    
class T:
    def __init__(self, pos, shape=None):
        self.pos = pos
        self.neighbors = {d: None for d in D.directions}
        self.shape = shape
        if shape:
            self.superpos = set()
            self.neighbor_options = shape.neighbor_options
        else:
            self.superpos = D.all_prototypes.copy()
            self.neighbor_options = {d: D.all_prototypes.copy() for d in D.directions}
        #print("Os", self.options)
        #print("BOs", self.barrier_options)

    def updateNeighborOptions(self):
        if self.shape: return
        #print("updateNeighborOptions")
        progress = {d: set() for d in D.directions}
        for potential_shape in self.superpos:
            for d in D.directions:
                progress[d] = progress[d].union(potential_shape.neighbor_options[d])
        self.neighbor_options = progress
        #print(self.neighbor_options)

    def setShape(self, shape):
        self.superpos = set()
        self.shape = shape
        self.neighbor_options = shape.neighbor_options
    
    def __repr__(self):
        return f"<Tile at {self.pos} with contents {self.shape}>"

    def __str__(self):
        return f"<Tile at {self.pos} with contents {self.shape}>"

class HexSheet:
    
    def draw_sheet(self, screen):
        #screen.blit(self.hexx, (0, 0))
        #return
        #for j, row in enumerate(self.sheet):
            #for tile in row:
            #for i, t in enumerate(row):
        cx, cy = screen.get_width() // 2 - X // 2, screen.get_height() // 2 - Y // 2
        self.screen = screen.get_width(), screen.get_height()
        inverty = -1 if True else 1
        for (i, j), t in self.sheet.items():
            if not self.drawn: print(f"({i}, {j}) {t.shape}, {len(t.superpos)}")
            if t.shape:
                y, x = t.shape.sprite
            else:
                if t.superpos:
                    y, x = 0, 1 # Transparent
                    L = len(t.superpos) - 1
                    L = 17 if L > 17 else L
                    y, x = 5 + L // 6, L % 6
                    if not self.drawn: print(L)
                    if not self.drawn: print(f"Sprite: {L}, ({y}, {x})")
                else:
                    y, x = 0, 0 # Error
            sprite = self.tiles[y][x]
            screen.blit(sprite, (
                    cx + (i*(X-6)), 
                    cy + inverty * (j*Y - i*(Y/2))
                    ))
        self.drawn = True
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        self.mouse_x, self.mouse_y = self.mouse_x // self.scale_factor, self.mouse_y // self.scale_factor
        if self.mouse_x != self.mouse_x_prev or self.mouse_y != self.mouse_y_prev:
            #print(f"mouse: ({self.mouse_x}, {self.mouse_y})")
            self.mouse_i = (self.mouse_x - cx) // (X-6)
            i_soft = (self.mouse_x - cx) / (X-6)
            self.mouse_j = int((((self.mouse_y - cy) + inverty*self.mouse_i*(Y/2)) // Y) * inverty)
            j_soft = (((self.mouse_y - cy) + inverty*self.mouse_i*(Y/2)) / Y) * inverty
            self.mouse_defined=True
            #print(i_soft, j_soft)
        if self.mouse_defined:
            screen.blit(self.tiles[0][3], (
                    cx + (self.mouse_i*(X-6)), 
                    cy + inverty * (self.mouse_j*Y - self.mouse_i*(Y/2))
                    ))
        self.mouse_x_prev, self.mouse_y_prev = self.mouse_x, self.mouse_y

    def print_info(self):
        inverty = -1 if True else 1
        if self.mouse_defined:
            i, j = self.mouse_i, self.mouse_j
            print(f"Tile at {(i, j)}")
            if (i, j) in self.sheet:
                t = self.sheet[(i, j)]
                print(t)
                for option in t.superpos:
                    print(' ', option)
                print()
                for d, neighbor_superpos in t.neighbor_options.items():
                    print(f"{d}: {neighbor_superpos} {len(neighbor_superpos)}")
            else:
                print("Unexplored")
            #cx + (self.mouse_i*(X-6)), 
            #cy + inverty * (self.mouse_j*Y - self.mouse_i*(Y/2))
        #self.mouse_x_prev, self.mouse_y_prev = self.mouse_x, self.mouse_y
        
    def getNeighborCoords(self, c):
        x, y = c
        #           NW        SW         S          SE        NE         N
        return {(x-1, y), (x-1, y-1), (x, y-1), (x+1, y), (x+1, y+1), (x, y+1)}

    def addTileToSheet(self, pos):
        # Adds an empty tile to the sheet
        new = T(pos)
        self.sheet[pos] = new
        self.frontier.add(new)
        neighborCoords = self.getNeighborCoords(pos)
        for neighborC in neighborCoords:
            if neighborC in self.sheet:
                neighbor = self.sheet[neighborC]
                relativeDir = getDirectionFromRelativeCoords(pos, neighborC)
                reverseDir = D.links[relativeDir]
                new.neighbors[relativeDir] = neighbor
                neighbor.neighbors[reverseDir] = new
        return new
        
    def addHexToSheet(self, pos, hexType):
        if pos not in self.sheet or self.sheet[pos].shape:
            print("Hex already filled or missing")
            return
        h = self.sheet[pos]
        if hexType in h.superpos:
            print(f"\n\nfilling {pos} with {hexType}\n\n")
            # Sets the shape of the tile
            h.setShape(hexType)
            # Update the borders of the tile to be 
            self.frontier.remove(h)
        else:
            print(f"Shape {hexType} not in {h.superpos}")
            c = input("Continue anyway? ")
            if c == "n":
                exit()

        h.updateNeighborOptions()

        neighborCoords = self.getNeighborCoords(pos)
        # print("NC", neighborCoords)
        # If it doesn't have neighbors, create them
        # print(h.neighbor_options)
        for neighborC in neighborCoords:
            if neighborC not in self.sheet:
                new = self.addTileToSheet(neighborC)
            d = getDirectionFromRelativeCoords(pos, neighborC)
            self.update_list.append((self.sheet[neighborC], d))
        self.clear_update_list()

    def clear_update_list(self):
        while len(self.update_list) and self.state >= 0:
            self.process_update_list()

    def process_update_list(self):
        processing, changed_direction = self.update_list.pop()
        startingOptionCount = len(processing.superpos)
        #print(f"Updating {processing} from {changed_direction}")
        if processing.shape:
            #print(f"Tile already set")
            return

        # TODO
        for o in D.all_prototypes:
            for d in D.directions:
                n = processing.neighbors[d]
                if not n:
                    # Empty neighbor, do nothing?
                    pass
                else:
                    ns_neighbor_options = n.neighbor_options[D.links[d]]
                    processing.superpos = processing.superpos.intersection(ns_neighbor_options)
                    # Share possibility space
                    if not processing.superpos:
                        print("InValid Hex State Issue")
                        self.state = -1
                        # exit()
                    pass

        if startingOptionCount > len(processing.superpos):
            # Changed list, update neighbors
            processing.updateNeighborOptions()
            neighborCoords = self.getNeighborCoords(processing.pos)
            for neighborPos in neighborCoords:
                if neighborPos not in self.sheet:
                    self.addTileToSheet(neighborPos)
                self.update_list.append((self.sheet[neighborPos], None))
                #print(d, n)
                pass
        elif startingOptionCount < len(processing.superpos):
            print("Massive error")
            print(f"Room started with {startingOptionsCount} options and now has {len(processing.superpos)}")
            print("That shouldn't be able to happen")
            exit()


    def getNeighbor(self, pos, direction):
        x, y = pos

        if direction == "NE" or direction == "SE":
            x += 1
        elif direction == "NW" or direction == "SW":
            x += -1

        if direction == "N" or direction == "NE":
            y += 1
        elif direction == "S" or direction == "SW":
            y += -1
        if (x, y) in self.sheet:
            return self.sheet[(x, y)]
        return None

    def collapseSingleProb(self):
        print("Collapsing prob")
        priority_frontier = sorted(self.frontier, key=lambda t: len(t.superpos))
        min_priority = len(priority_frontier[0].superpos)
        i = 0
        cap = len(priority_frontier)
        while i < cap and len(priority_frontier[i].superpos) == min_priority: i += 1
        min_priority_frontier = priority_frontier[0:i]
        nearest_frontier = sorted(min_priority_frontier, key=lambda t: hex_manhatten((0, 0), t.pos))
        most_restricted = nearest_frontier[0]
        print(most_restricted, len(most_restricted.superpos))
        # TODO add some way to center it around a certain locale, or keep it on screen
        ordered_superpos = list(most_restricted.superpos)
        ordered_weights = [o.weight for o in ordered_superpos]

        choice = random.choices(ordered_superpos, weights=ordered_weights)[0]
        self.addHexToSheet(most_restricted.pos, choice)

    def update_tick(self):
        if self.state < 0:
            return self.state
        if len(self.update_list):
            self.process_update_list()
        else:
            self.collapseSingleProb()
        print(f"to_update: {len(self.update_list)}")
        if not self.update_list:
            print("Culling offscreen tiles")
            wx, wy = self.screen
            wx, wy = wx // 2, wy // 2
            def on_screen(pos):
                i, j = pos
                onscreen = wx >= abs((i*(X-6))) and wy >= abs(j*Y - i*(Y/2))
                if not onscreen: print(f"Culling {pos}")
                return onscreen
            self.frontier = {t for t in self.frontier if on_screen(t.pos)}
            if not self.frontier:
                self.state = -1
                return

    def debug(self):
        print("\n\n\n-----DEBUG-----\n\n")
        for coord, tile in self.sheet.items():
            print()
            print(coord)
            print(tile)
            print(tile.superpos)
        print("\n\n\n-----DEBUG OVER-----\n\n")
        
    def initSheet(self, hexType = None):
        if not hexType:
            self.addTileToSheet((0, 0))
            self.addHexToSheet((0, 0), D.Straight_N)
            #self.debug()
            #self.addHexToSheet((0, 1), D.Straight_N)
            #self.addHexToSheet((1, 1), D.Shelf_NW)
            #self.collapseSingleProb()
            #self.collapseSingleProb()
            #self.debug()

    def setSheet(self, inSheet):
        self.sheet = inSheet

    def __init__(self, tilesheet, scale=4, debug=False):
        self.drawn = False
        self.hexx = tilesheet.convert_alpha()
        self.hexrect = self.hexx.get_rect()
        self.sheet = {}
        self.frontier = set()
        self.scale_factor = scale
        self.mouse_defined=False
        self.state = 0
        # (Tile, direction) where direction corresponds to the direction that Tile was updated from
        # i.e. going direction FROM Tile will get you to the changed tile that added it
        self.update_list = []
        #n1 = self.addHexToSheet((0, 0), D.Circle)
        #print("VBs", getValidNeighborsWithBarrier("D", n.shape.barrier_options["N"]))
        self.tiles = []
        for j in range(8):
            tmp = []
            for i in range(6):
                t = pygame.Surface((X, Y)).convert_alpha()
                t.fill((0, 0, 0, 0))
                t.blit(self.hexx, (0, 0), (X * i, Y * j, X, Y))
                tmp += [t]
            self.tiles += [tmp]
        print(self.tiles)
        if debug:
            #return # TODO remove
            pass
        self.mouse_x_prev, self.mouse_y_prev = pygame.mouse.get_pos()
        self.initSheet()
