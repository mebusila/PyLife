__author__ = 'mebus'
__email__  = 'sherban.carlogea@gmail.com'

from life import Life

class Blinker(Life):

    grid_size = [20, 20]

    def initial_seed(self):
        return [(9, 8), (9, 9), (9, 10)]

if __name__ == "__main__":
    Blinker().run()