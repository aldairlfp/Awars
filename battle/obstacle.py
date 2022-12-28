class Obstacle(object):
    def __init__(self, x, y, width, height):
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def get_size(self):
        return self._width, self._height

    def get_pos(self):
        return self._x, self._y
