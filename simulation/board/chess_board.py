from simulation.units.chess_pieces import *

class Chess_board():
    def __init__(self) -> None:
        self._board = None
        
    def cell(self, pos):
        return self._board[pos[0]][pos[1]]
        
    def set_cell(self, pos, value):
        self._board[pos[0]][pos[1]] = value
    
    def __str__(self) -> str:
        board = '  _    _    _    _    _    _    _    _  '
        for row in self._board:
            board += '\n'
            for cell in row:
                if cell != None:
                    board += ' ' + str(cell) + ' '
                else:
                    board += ' |_| ' 
        return board
        
    def board(self):
        return self._board
    
    def board_s(self, board):
        try:
            if len(board) == 8:
                for row in board:
                    if len(row) != 8:
                        print('Board must be 8x8')
                        return None
                self._board = board
            else:
                print('Board must be 8x8')
                return None
        except AttributeError:
            print('Some error with board shape')
            return None

    def height(self):
        return 8
    
    def width(self):
        return 8
