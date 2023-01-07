from simulation.board.maps_gen.chess_generator import chess_generator
from simulation.modes.modes import Mode
from simulation.board.chess_board import Chess_board

class Chess_mode(Mode):
    def __init__(self):
        super().__init__()
        self._map = chess_generator()
        self._name = 'chess'
        
    def generate_board(self, height, width, board_gen = chess_generator):
        if height != 8 or width != 8:
            print('Board must be 8x8')
            return None 
        else:
            self._map = board_gen(height, width)
            board = Chess_board()
            board.board_s(self._map)
            return board
        
    def win_condition(self, simulation):
        team_white = []
        team_black = []
        
        king_white = None
        king_black = None
        
        board = simulation.board_s()
        
        for row in board.board():
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
    
    def action_validator(self, board, unit, action):
        if not unit.team_s() is 'white' or not unit.team_s() is 'black':
            return False, 'Invalid team'
            
        team = None
        if unit.team_s() is 'white':
            team = self._get_team('black', board)
        else:
            team = self._get_team('white', board)
            
        king = None
        for unit in unit.pieces():
            if unit.name() is 'king':
                king = unit
                break
        
        copy = Chess_board()
        self._copy_board(board, copy)
            
        piece = board.cell(unit.pos_s())
        
        copy[action[1][0]][action[1][1]] = piece
        copy[action[0][0]][action[0][1]] = None
        
        check, v, k = self._is_check(team, king, copy)
        
        if check:
            return False, 'Invalid move, your king is in check'
        
        board.set_cell(action[1], piece)
        board.set_cell(action[0], None)
        piece.pos_s(action[1])
        
        return True, f'Valid move, from [{action[0][0]}, {action[0][1]}] to [{action[1][0]}, {action[1][1]}]'
        
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