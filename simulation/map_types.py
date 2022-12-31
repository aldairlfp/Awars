from board import Cell

class Basic_map():
    def __init__(self, board):
        self._height = board.get_height()
        self._width = board.get_width()
        self._map = [[Cell((i, j), None, "sunny") for i in range(self._width)] for j in range(self._height)]
    
    def generate_map(self):
        for i in range(self._height):
            for j in range(self._width):
                self._map[i][j].set_terrain(("grass", 1), 0)
        
        return self._map

