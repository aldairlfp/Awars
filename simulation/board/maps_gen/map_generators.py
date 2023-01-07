from simulation.board.board import Cell
from simulation.board.weathers import *

def normal_map(height, width):
    map = [[Cell(None, Sunny()) for i in range(width)] for j in range(height)]
    for i in range(height):
        for j in range(width):
            map[i][j].terrain(("grass", 1), 0)
       
    return map