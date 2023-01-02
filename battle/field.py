import unit


class Field:
    def __init__(self, width=10, height=10, obstacles=None):
        self._field = {}
        self._width = width
        self._height = height
        if obstacles is not None:
            for obstacle in obstacles:
                self._field[obstacle.get_x(), obstacle.get_y()] = obstacle

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

    def get_obstacles(self):
        return self._obstacles

    def get_obstacles_count(self):
        return len(self._obstacles)

    def get_obstacle(self, x, y):
        for obstacle in self._obstacles:
            if obstacle.get_x() <= x < obstacle.get_x() + obstacle.get_width() and obstacle.get_y() <= y < obstacle.get_y() + obstacle.get_height():
                return obstacle
        return None

    def get_obstacle_at(self, x, y):
        for obstacle in self._obstacles:
            if obstacle.get_x() == x and obstacle.get_y() == y:
                return obstacle
        return None

    def add_obstacle(self, obstacle):
        self._obstacles.append(obstacle)

    def remove_obstacle(self, obstacle):
        self._obstacles.remove(obstacle)

    def __contains__(self, item):
        if item in self._field:
            return True
        else:
            return False
