#!/usr/bin/python3

import sys, pygame
from screeninfo import get_monitors

from hexTiles.Defaults import Defaults as D

import game
import hexSheet
from characters import fromg

if __name__ == "__main__":

    # Set window dimensions
    window_size = window_w, window_h = 1200, 800

    # Set window position to middle
    white = 255, 255, 255
    m_width, m_height = 0, 0
    scale_factor = 1
    for m in get_monitors():
        m_width, m_height = m.width, m.height
    window_x, window_y = (m_width-window_w)/2, (m_height-window_h)/2

    a = fromg.Fromg()
    pygame.init()
    screen = pygame.display.set_mode(window_size)
    grid = pygame.Surface((window_w//scale_factor, window_h//scale_factor)).convert_alpha()
    grid.fill(white)
    h = hexSheet.HexSheet(pygame.image.load("../images/hex-tiles-with-nooks.png"), scale=scale_factor, debug=True)
    s = {}
    sGrid = [
                [D.Void, D.Wheel_N, D.Shelf_N, D.Wheel_N],
                [D.Wheel_S, D.Void, D.Straight_NE, D.Circle],
                [D.Shelf_NE, D.Shelf_N, D.Circle, D.Circle],
                [D.Shelf_S, D.Straight_SE, D.Circle, D.Shelf_SW]
            ]
    sGrid = sGrid[::-1]

    xOffset = len(sGrid[0]) // 2
    yOffset = len(sGrid) // 2
    print("Offsets:", xOffset, yOffset)

    for j, row in enumerate(sGrid):
        for i, item in enumerate(row):
            print("adding", item)
            pos = (i - xOffset, j - yOffset)
            s[pos] = hexSheet.T(pos, item)

    # h.sheet = s
    # h.addTileToSheet((2, 2))
    # h.addTileToSheet((2, 3))
    # h.addTileToSheet((1, 2))
    # h.addTileToSheet((0, 2))

    autogen = False
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("Space pressed!")
                    h.update_tick()
                if event.key == pygame.K_RETURN:
                    print("Return pressed!")
                    autogen = not autogen
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event)
                if event.button == 1:
                    print("Clicked!")
                if event.button == 3:
                    print("Right Clicked!")
                    h.print_info()
        
        if autogen:
            h.update_tick()
        if h.state < 0:
            autogen=False
        grid.fill(white)
        h.draw_sheet(grid)
        screen.blit(pygame.transform.scale(grid, screen.get_rect().size), (0, 0))
        pygame.display.flip()
