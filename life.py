__author__ = 'Serban Carlogea'
__email__  = 'sherban.carlogea@gmail.com'

from display import Display
import sys
import random


class Life(object):

    __display = None
    grid_size = [100, 100]

    def __init__(self):
        self.__display = Display(title='PyLife', grid_size=self.grid_size, width=800, height=800)

    def initial_seed(self):
        cells = {}
        for x in range(self.grid_size[0]):
            for y in range(self.grid_size[1]):
                if random.randint(0, 1) == 1:
                    cells[(x, y)] = 1
        return cells


    def get_cell_neighbours(self, item, cells):
        neighbours = 0
        for x in range(-1, 2):
            for y in range(-1, 2):
                cell = (item[0] + x, item[1] + y)
                if cell[0] in range(0, self.grid_size[0]) and cell[1] in range(0, self.grid_size[1]) and cell in cells:
                    if (x == 0 and y == 0) is False:
                        neighbours += 1
        return neighbours

    def get_cells(self, cells):
        new_cells = {}
        for x in range(self.grid_size[0]):
            for y in range(self.grid_size[1]):
                neighbours = self.get_cell_neighbours((x, y), cells)
                if ((x, y) in cells) and (neighbours == 2 or neighbours == 3):
                    new_cells[(x, y)] = 1
                elif ((x, y) in cells) is False and neighbours == 3:
                    new_cells[(x, y)] = 1
        return new_cells

    def run(self):
        cells = self.initial_seed()
        while True:
            cells = self.get_cells(cells)
            for cell in cells:
                self.__display.draw(cell[0], cell[1])
            if self.__display.update() is False:
                self.__display.quit()
                sys.exit(0)
