__author__ = 'mebus'
__email__  = 'sherban.carlogea@gmail.com'

from life import Life

class Blinker(Life):

    grid_size = [20, 20]

    def initial_seed(self):
        cells = {}

        cells[9, 8] = 1
        cells[9, 9] = 1
        cells[9, 10] = 1

        return cells

if __name__ == "__main__":
    Blinker().run()