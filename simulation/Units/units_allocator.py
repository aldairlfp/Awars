from random import randint
from simulation.units.chess_pieces import *
from simulation.units.unit import Chess_unit

def random_allocator(board, units):
    for unit in units:
        pos_x = randint(0, board.height() - 1)
        pos_y = randint(0, board.width() - 1)
        
        while not board.map()[pos_x][pos_y].units(unit):
            pos_x = randint(0, board.height() - 1)
            pos_y = randint(0, board.width() - 1)
        
        unit.pos((pos_x, pos_y))

    return units
    
def chess_allocator(board, units):
    if len(units) != 2:
        print('There must be 2 players')
        return None
        
    for unit in units:
        for piece in unit.pieces():
            board.set_cell(piece.pos(), piece)
    
    
        
    
    