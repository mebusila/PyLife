__author__ = 'mebus'
__email__  = 'sherban.carlogea@gmail.com'

from life import Life

class Beacon(Life):

    grid_size = [20, 20]

    def initial_seed(self):
        return {
            (7, 9), (7, 10), (8, 10),
            (10, 8), (10,7), (9, 7)
        }

if __name__ == "__main__":
    Beacon().run()