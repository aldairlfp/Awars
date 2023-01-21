from algorithms.utils.search import chess_in_board

class Chess_piece():
    def __init__(self, pos, name, color, value = 1):
        self._pos = pos
        self._name = name
        self._color = color
        self._value = value
        
    def pos(self):
        return self._pos
        
    def value(self):
        return self._value
        
    def pos_s(self, pos):
        self._pos = pos
    
    def name(self):
        return self._name
    
    def color(self):
        return self._color
    
    def play(self, board):
        pass
        
    def team_s(self):
        return self._color
        
    def __str__(self):
        return self._name[0] + '_' + self._color[0]
    
        
class Pawn(Chess_piece):
    def __init__(self, pos, color):
        super().__init__(pos, 'pawn', color)
        self._first_move = True
        
    def play(self, board):
        movs = []
        
        new_pos = (self._pos[0] + 1, self._pos[1])
        if chess_in_board(board, new_pos) and board.cell(new_pos) == None:
            movs.append((self._pos, new_pos))
            
        new_pos = (self._pos[0] + 1, self._pos[1] + 1)
        
        if chess_in_board(board, new_pos) and board.cell(new_pos) != None and board.cell(new_pos).color() != self._color:
            movs.append((self._pos, new_pos))
            
        new_pos = (self._pos[0] + 1, self._pos[1] - 1)
        
        if chess_in_board(board, new_pos) and board.cell(new_pos) != None and board.cell(new_pos).color() != self._color:
            movs.append((self._pos, new_pos))
            
        
        if self._first_move:
            new_pos = (self._pos[0] + 2, self._pos[1])
            if chess_in_board(board, new_pos) and board.cell(new_pos) == None:
                movs.append((self._pos, new_pos))

            self._first_move = False

        return movs
        
class Rook(Chess_piece):
    def __init__(self, pos, color):
        super().__init__(pos, 'Rook', color, 5)
        self._first_move = True
        
    def play(self, board):
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        movs = []
        
        for dir in dirs:
            while True:
                new_pos = (self._pos[0] + dir[0], self._pos[1] + dir[1])
                if chess_in_board(board, new_pos):
                    if board.cell(new_pos) == None:
                        movs.append((self._pos, new_pos))
                        new_pos = (self._pos[0] + dir[0], self._pos[1] + dir[1])
                    elif board.cell(new_pos).color() != self._color:
                        movs.append((self._pos, new_pos))
                        break
                    else:
                        break
                else:
                    break
                    
        return movs
        
class Bishop(Chess_piece):
    def __init__(self, pos, color):
        super().__init__(pos, 'bishop', color, 3)
        
    def play(self, board):
        dirs = [(1, -1), (1, 1), (-1, 1), (-1, -1)]
        movs = []
        
        for dir in dirs:
            new_pos = (self._pos[0] + dir[0], self._pos[1] + dir[1])
            while chess_in_board(board, new_pos):
                if board.cell(new_pos) == None:
                    movs.append((self._pos, new_pos))
                    new_pos = (self._pos[0] + dir[0], self._pos[1] + dir[1])
                elif board.cell(new_pos).color() != self._color:
                    movs.append((self._pos, new_pos))
                    break
                else:
                    break

class Knight(Chess_piece):
    def __init__(self, pos, color):
        super().__init__(pos, 'knight', color, 3)
        
    def play(self, board):
        dirs = [(1, -2), (1, 2), (-1, 2), (-1, -2), (2, -1), (2, 1), (-2, 1), (-2, -1)]
        movs = []
        
        for dir in dirs:
            new_pos = (self._pos[0] + dir[0], self._pos[1] + dir[1])
            if chess_in_board(board, new_pos):
                if board.cell(new_pos) == None:
                    movs.append((self._pos, new_pos))
                elif board.cell(new_pos).color() != self._color:
                    movs.append((self._pos, new_pos))
                    
        return movs
        
class Queen(Chess_piece):
    def __init__(self, pos, color):
        super().__init__(pos, 'queen', color, 9)
        
    def play(self, board):
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (1, 1), (-1, 1), (-1, -1)]
        movs = []
        
        for dir in dirs:
            while True:
                new_pos = (self._pos[0] + dir[0], self._pos[1] + dir[1])
                if chess_in_board(board, new_pos):
                    if board.cell(new_pos) == None:
                        movs.append((self._pos, new_pos))
                        new_pos = (self._pos[0] + dir[0], self._pos[1] + dir[1])
                    elif board.cell(new_pos).color() != self._color:
                        movs.append((self._pos, new_pos))
                        break
                    else:
                        break
                else:
                    break

class King(Chess_piece):
    def __init__(self, pos, color):
        super().__init__(pos, 'king', color, 100)
        
    def play(self, board):
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (1, 1), (-1, 1), (-1, -1)]
        movs = []
        
        for dir in dirs:
            new_pos = (self._pos[0] + dir[0], self._pos[1] + dir[1])
            if chess_in_board(board, new_pos):
                if board.cell(new_pos) == None:
                    movs.append((self._pos, new_pos))
                elif board.cell(new_pos).color() != self._color:
                    movs.append((self._pos, new_pos))
                    
    def __str__(self):
        return 'K_' + self._color[0]
        
