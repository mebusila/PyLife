__author__ = 'Serban Carlogea'
__email__  = 'sherban.carlogea@gmail.com'

from display import Display
import sys
import random


class Life(object):

    __display = None
    grid_size = [80, 80]

    def __init__(self):
        self.__display = Display(title='PyLife', grid_size=self.grid_size, width=800, height=800)

    def initial_seed(self):
        cells = {}
        for x in range(self.grid_size[0]):
            for y in range(self.grid_size[1]):
                if random.randint(0, 1):
                    cells[x, y] = 1
        return cells


    def get_cell_neighbours(self, item, cells):
        neighbours = 0
        for x in range(-1, 2):
            for y in range(-1, 2):
                cell = (item[0] + x, item[1] + y)
                if cell[0] in range(0, self.grid_size[0]) and cell[1] in range(0, self.grid_size[1]):
                    try:
                        if cells[cell] == 1:
                            if x == 0 and y == 0:
                                pass
                            else:
                                neighbours += 1
                    except KeyError:
                        pass
        return neighbours

    def get_cells(self, cells):
        new_cells = {}
        for x in range(self.grid_size[0]):
            for y in range(self.grid_size[1]):
                neighbours = self.get_cell_neighbours((x, y), cells)
                try:
                    if (neighbours == 2 or neighbours == 3) and cells[(x, y)] == 1:
                        new_cells[(x, y)] = 1
                except KeyError:
                    if neighbours == 3:
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
