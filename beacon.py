__author__ = 'mebus'
__email__  = 'sherban.carlogea@gmail.com'

from life import Life

class Beacon(Life):

    grid_size = [20, 20]

    def initial_seed(self):
        cells = self.fill_grid()

        cells[7, 9] = 1
        cells[7, 10] = 1
        cells[8, 10] = 1

        cells[10, 8] = 1
        cells[10, 7] = 1
        cells[9, 7] = 1

        return cells

if __name__ == "__main__":
    Beacon().run()