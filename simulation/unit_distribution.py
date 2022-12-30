from unit import Unit
from random import randint

class Basic_distribution():
    def __init__(self, board, units):
        self._height = board.get_height()
        self._width = board.get_width()
        self._map = board.get_map()
        self._units = board.get_units()
        
    def generate_units(self):
        for unit in self._units:
            pos_x = randint(0, self._height - 1)
            pos_y = randint(0, self._width - 1)
            try:
                if self._map[pos_x][pos_y].set_unit(unit):
                    pass
                else:
                    raise IndexError("The cell is already occupied")
            except IndexError:
                raise IndexError("Invalid position")
        
        return self._units