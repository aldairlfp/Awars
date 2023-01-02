from random import randint

def random_allocator(units, board):
    for unit in units:
        pos_x = randint(0, board.height() - 1)
        pos_y = randint(0, board.width() - 1)
        try:
            if board.map()[pos_x][pos_y].unit(unit):
                unit.pos((pos_x, pos_y))
            else:
                raise IndexError("The cell is already occupied")
        except IndexError:
            pass
        
    return units