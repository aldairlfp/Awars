import unit


class Field:
    def __init__(self, width=10, height=10):
        self.field = {}
        self.width = width
        self.height = height

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        str = ''
        for i in range(self.width):
            for j in range(self.height):
                str += '  '
                if (i, j) in self.field:
                    if self.field[i, j] in self.soldiers.values():
                        str += 'S'
                    else:
                        str += 'W'
                else:
                    str += '.'
            str += '\n'
        return str
