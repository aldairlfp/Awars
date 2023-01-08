from algoritms.strategies.chess_evaluator import chess_evaluator
from simulation.board.chess_board import Chess_board

class Chess_strategy():
    def __init__(self, unit, evaluator):
        self._board = None
        self._evaluator = evaluator
        self._unit = unit
        
    def board(self, board):
        self._board = board
        

class Minimax_strategy(Chess_strategy):

    def __init__(self, unit, depth = 5):
        super().__init__(unit, chess_evaluator)
        self._depth = depth
        
    def play(self, movs):
        movs = sorted(movs, key = lambda x: self._mini_max(x, self._board, 0, self._depth), reverse=True)
        
        return movs            
        
    def _mini_max(self, mov, board, value, depth):
        copy = self._copy(board)
        
        piece = copy.cell([mov[0][0]][mov[0][1]])
        
        copy[mov[1][0]][mov[1][1]] = piece
        copy[mov[0][0]][mov[0][1]] = None
        
        current = 0
        
        piece.pos_s(mov[1])
        
        is_terminal, message = self._win_condition(copy)
        
        if is_terminal:
            if self._unit.team_s() in message.lower():
                piece.pos_s(mov[0])
                value += 100
                return value
            piece.pos_s(mov[0])
            value -= 100
            return value
            
        if depth == 0:
            value += self._evaluator(piece, copy)
            piece.pos_s(mov[0])
            return value
        
        team = [piece for piece in self._get_pieces(self._unit.team_s(), board)]
        
        movs = []
        
        for piece in team:
            movs.extend(piece.play(copy))
        
        current = self._evaluator(team, copy)
        
        if self._depth %2 == 0:
            if depth % 2 == 0:
                for mov in movs:
                    current += self._mini_max(mov, copy, value, depth - 1)
                value += current
            else:
                for mov in movs:
                    current -= self._mini_max(mov, copy, value, depth - 1)
                value += current
        else:
            if depth % 2 == 0:
                for mov in movs:
                    current -= self._mini_max(mov, copy, value, depth - 1)
                value += current
            else:
                for mov in movs:
                    current += self._mini_max(mov, copy, value, depth - 1)
                value += current
                
        piece.pos_s(mov[0])
        return value
            
    def _get_pieces(self, team, board):
        for row in board:
            for cell in row:
                if cell != None and cell.color() == team:
                    yield cell
                    
    def _copy(self, board):
        copy = Chess_board()
        map = []
        for row in board.board():
            map.append([])
            for cell in row:
                map[-1].append(cell)
        copy.board_s(map)
        return copy
        
    def _win_condition(self, board):
        team_white = []
        team_black = []
        
        king_white = None
        king_black = None
        
        for row in board:
            for cell in row:
                if cell != None:
                    if cell.team_s() in 'white':
                        team_white.append(cell)
                        if cell.name() is 'king':
                            king_white = cell
                    else:
                        team_black.append(cell)
                        if cell.name() is 'king':
                            king_black = cell
                            
        white_movs = []
        black_movs = []
        
        check_white, check_black = None, None
        
        white, check_white, white_movs = self._is_check(team_white, king_black, board)
        black, check_black, black_movs = self._is_check(team_black, king_white, board)
        
        check_white_path = None
        check_black_path = None
        
        if white:
            check_white_path = self._check_path(check_white, board)
            if self._is_checkmate(check_white_path, black_movs, team_white, king_white, board):
                return True, 'Black won'
            else:
                return False, 'White is in check, but can escape'
        if black:
            check_black_path = self._check_path(check_black, board)
            if self._is_checkmate(check_black_path, white_movs, team_black, king_black, board):
                return True, 'White won'
            else:
                return False, 'Black is in check, but can escape'
        
        return False, 'No winner'
    
    def _is_check(self, team, king, board):
        movs = []
        
        for unit in team:
            new_movs = unit.play(board)
            if new_movs != None:
                movs += unit.play(board)
            
        for mov in movs:
            if mov[1][0] == king.pos()[0] and mov[1][1] == king.pos()[1]:
                return True, mov, movs
                
        return False, None, None
        
    def _is_checkmate(self, check_pos, enemy_movs, team, king, board):
        movs = []
        king_movs = king.play(board)
        for unit in team:
            if unit.pos_s()[0] == king.pos_s()[0] and unit.pos_s()[1] == king.pos_s()[1]:
                continue
            movs += unit.play(board)
            
        for mov in movs:
            for pos in check_pos:
                if mov[1][0] == pos[1][0] and mov[1][1] == pos[1][1]:
                    return False
        
        can_move = False
        
        for mov in king_movs:
            can_move = True
            for enemy_mov in enemy_movs:
                if mov[1][0] == enemy_mov[1][0] or mov[1][1] == enemy_mov[1][1]:
                    can_move = False
                    break
                    
        return not can_move
            
    def _check_path(self, mov, board):
        piece = board[mov[0]]
        direction = [] 
        current_pos = mov[0]
        
        if piece.name() == 'knight':
            return [mov]
        elif piece.name() == 'pawn':
            return [mov]
        elif piece.name() == 'queen':
            if mov[0][0] > mov[1][0]:
                direction.append(-1)
            elif mov[0][0] < mov[1][0]:
                direction.append(1)
            else: 
                direction.append(0)
            if mov[0][1] > mov[1][1]:
                direction.append(-1)
            elif mov[0][1] < mov[1][1]:
                direction.append(1)
            else:
                direction.append(0)
            path = []
            while current_pos[0] != mov[1][0] and current_pos[1] != mov[1][1]:
                current_pos = (current_pos[0] + direction[0], current_pos[1] + direction[1])
                path.append(mov[0], current_pos)
            return path
        elif piece.name() == 'bishop':
            if mov[0][0] > mov[1][0]:
                direction.append(-1)
            elif mov[0][0] < mov[1][0]:
                direction.append(1)
            else: 
                direction.append(0)
            if mov[0][1] > mov[1][1]:
                direction.append(-1)
            elif mov[0][1] < mov[1][1]:
                direction.append(1)
            else:
                direction.append(0)
            path = []
            while current_pos[0] != mov[1][0] and current_pos[1] != mov[1][1]:
                current_pos = (current_pos[0] + direction[0], current_pos[1] + direction[1])
                path.append(mov[0], current_pos)
            return path
        elif piece.name() == 'rook':
            if mov[0][0] > mov[1][0]:
                direction.append(-1)
            elif mov[0][0] < mov[1][0]:
                direction.append(1)
            else: 
                direction.append(0)
            if mov[0][1] > mov[1][1]:
                direction.append(-1)
            elif mov[0][1] < mov[1][1]:
                direction.append(1)
            else:
                direction.append(0)
            path = []
            while current_pos[0] != mov[1][0] and current_pos[1] != mov[1][1]:
                current_pos = (current_pos[0] + direction[0], current_pos[1] + direction[1])
                path.append(mov[0], current_pos)
            return path
        
        return None
        
    def _copy_board(board, copy):
        for row in range(8):
            for col in range(8):
                copy.set_cell([row][col], board.cell([row][col]))
                
    def _get_team(self, team, board):
        allies = []
        for row in range(8):
            for col in range(8):
                if board[row][col] is not None and board[row][col].team_s() is team:
                    allies.append(board[row][col])
        return allies