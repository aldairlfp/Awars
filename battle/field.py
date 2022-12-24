class Field:
    def __init__(self, width=10, height=10):
        self.field = {}
        self.soldiers = {}
        self.soldiers_count = 0
        self.width = width
        self.height = height

    def add_soldier(self, soldier):
        self.soldiers_count += 1
        self.soldiers[soldier.get_posx(), soldier.get_posy()] = soldier
        self.field.update(self.soldiers)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        str = ''
        for i in range(self.width):
            for j in range(self.height):
                str += '  '
                if (i, j) in self.field:
                    str += 'S'
                else:
                    str += '.'
            str += '\n'
        return str
