from simulation.map_generators import normal_map
from simulation.action_exe import Action_executer

class Mode():
    def __init__(self) -> None:
        pass
    
    def generate_board(self, height, width, board_gen):
        return board_gen(height, width)
    
    def action_validator(self, board, unit, action):
        pass
    
    def win_condition(self, board):
        pass
    

class Normal_mode(Mode):
    def __init__(self) -> None:
        super().__init__()
    
    def win_condition(self, simulation):
        reaminings = []
        for unit in simulation.units():
            if unit.team() not in reaminings:
                reaminings.append(unit.team())
        
        if len(reaminings) == 1:
            return True, "Team " + str(reaminings[0]) + " won"
        else:
            return False, "No winner yet"
    
    def action_validator(self, board, unit, action):
        receiver = board.cell(action[1]).unit()
        end_pos = action[1]
        ini_pos = unit.pos()
        action_executer = Action_executer(unit, receiver, ini_pos, end_pos, action[0])
        if not receiver == None and receiver.team() == unit.team():
            return False, "Can't interact with allies"        
        
        if end_pos[0] < 0 or end_pos[0] > board.height() - 1 or end_pos[1] < 0 or end_pos[1] > board.width() - 1:
            return False, "Invalid position"
        else:
            action_executer.make_action(unit, board)
            return True, "Action executed"
            
    def calculate_offensive_power(self, basic, ini_pos, end_pos):
        return basic
    
    def calculate_defensive_power(self, basic, ini_pos, end_pos):
        return basic
    
    def calculate_movement_power(self, basic, ini_pos, end_pos):
        return basic
    
    def calculate_accuracy(self, basic, ini_pos, end_pos):
        return basic
        
    def generate_board(self, height, width, map_generator = normal_map):
        return super().generate_board(height, width, map_generator)
        
        
    
