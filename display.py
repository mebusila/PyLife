__author__ = 'Serban Carlogea'
__email__  = 'sherban.carlogea@gmail.com'

import pygame
from pygame.locals import *
from config import *

class Display(object):

    __display_surface = None
    __grid_bg_color =   GRID_BG_COLOR
    __grid_line_color = GRID_LINE_COLOR
    __alive_color =     LIVE_CELL_COLOR
    __dead_color =      DEAD_CELL_COLOR
    __fps =             FPS

    def __init__(self, title="Display", grid_size=None, width=WINDOW_WIDTH, height=WINDOW_HEIGHT):
        pygame.init()

        self.__cell_size = [1, 1]
        self.__grid_size = grid_size
        self.__width = width
        self.__height = height
        self.__cell_size[0] = self.__width  / self.__grid_size[0]+1
        self.__cell_size[1] = self.__height / self.__grid_size[1]+1
        self.__display_surface = pygame.display.set_mode((self.__width, self.__height))
        self.__display_surface.fill(self.__grid_bg_color)
        pygame.display.set_caption(title)

    def update(self):
        self.draw_grid()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                return False
        pygame.time.Clock().tick(self.__fps)
        return True

    def draw_grid(self):
        for x in range(0, self.__width, self.__cell_size[0]):
            pygame.draw.line(self.__display_surface, self.__grid_line_color, (x, 0), (x, self.__height))
        for y in range (0, self.__height, self.__cell_size[1]):
            pygame.draw.line(self.__display_surface, self.__grid_line_color, (0, y), (self.__width, y))

    def draw(self, x, y, is_alive):
        x *= self.__cell_size[0]
        y *= self.__cell_size[1]
        position = (x, y, self.__cell_size[0], self.__cell_size[1])
        if is_alive:
            pygame.draw.rect(self.__display_surface, self.__alive_color, position)
        else:
            pygame.draw.rect(self.__display_surface, self.__dead_color, position)

    def quit(self):
        pygame.quit()