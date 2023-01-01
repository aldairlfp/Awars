class Mode():
    def __init__(self, board_gen, map_generator) -> None:
        self._board_gen = board_gen
    
    def generate_board(self, height, width):
        return self._board_gen.generate_board(height, width)
    
    def action_validator(self, board, unit, action):
        pass
    
    def win_condition(self, board):
        pass
    
    def calculate_offensive_power(self, basic, ini_pos, end_pos):
        pass
    
    def calculate_defensive_power(self, basic, ini_pos, end_pos):
        pass
        
    def calculate_movement_power(self, basic, ini_pos, end_pos):
        pass
        
    def calculate_accuracy(self, basic, ini_pos, end_pos):
        pass

class Normal_mode(Mode):
    def __init__(self) -> None:
        super().__init__()
    
    def win_condition(self, board):
        reaminings = []
        for unit in board.get_units():
            if unit.get_team() not in reaminings:
                reaminings.append(unit.get_team())
        
        if len(reaminings) == 1:
            return True, "Team " + str(reaminings[0]) + " won"
        else:
            return False, "No winner yet"
    
    def action_validator(self, board, unit, action):
        is_ally = unit.get_team() == action.receiver.get_team()
        end_pos = action.get_end_pos()
        
        if is_ally:
            return False, "Can't interact with allies"
        elif end_pos[0] < 0 or end_pos[0] > board.get_height() - 1 or end_pos[1] < 0 or end_pos[1] > board.get_width() - 1:
            return False, "Invalid position"
        else:
            action.make_action(unit, board)
            return True, "Action executed"
            
    def calculate_offensive_power(self, basic, ini_pos, end_pos):
        return basic
    
    def calculate_defensive_power(self, basic, ini_pos, end_pos):
        return basic
    
    def calculate_movement_power(self, basic, ini_pos, end_pos):
        return basic
    
    def calculate_accuracy(self, basic, ini_pos, end_pos):
        return basic
