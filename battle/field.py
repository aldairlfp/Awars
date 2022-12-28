import unit


class Field:
    def __init__(self, width=10, height=10):
        self._field = {}
        self._width = width
        self._height = height

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def get_size(self):
        return self._width, self._height

    def get_cell(self, x, y):
        return self._field[x, y]

    def get_cells(self):
        return self._field
