#!/usr/bin/python3

import sys, pygame
from screeninfo import get_monitors

import game
import hexSheet
from characters import fromg

if __name__ == "__main__":
    print("Hello world!")

    # Set window dimensions
    window_size = window_w, window_h = 600, 400

    # Set window position to middle
    white = 255, 255, 255
    m_width, m_height = 0, 0
    for m in get_monitors():
        print(m)
        m_width, m_height = m.width, m.height
    window_x, window_y = (m_width-window_w)/2, (m_height-window_h)/2

    a = fromg.Fromg()
    pygame.init()
    screen = pygame.display.set_mode(window_size)
    grid = pygame.Surface((window_w//4, window_h//4)).convert_alpha()
    grid.fill(white)
    h = hexSheet.HexSheet(pygame.image.load("../images/hex-tiles.png"))

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        
        grid.fill(white)
        h.draw_sheet(grid)
        screen.blit(pygame.transform.scale(grid, screen.get_rect().size), (0, 0))
        pygame.display.flip()
