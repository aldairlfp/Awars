from random import randint

def random_allocator(board, units):
    for unit in units:
        pos_x = randint(0, board.height() - 1)
        pos_y = randint(0, board.width() - 1)
        
        while not board.map()[pos_x][pos_y].units(unit):
            pos_x = randint(0, board.height() - 1)
            pos_y = randint(0, board.width() - 1)
        
        unit.pos((pos_x, pos_y))

    return units