from simulation.map_generators import normal_map
from simulation.action_exe import Action_executer
from simulation.board import Board

class Mode():
    def __init__(self) -> None:
        pass
    
    def generate_board(self, height, width, board_gen):
        return  Board(board_gen(height, width))
    
    def action_validator(self, board, unit, action):
        pass
    
    def win_condition(self, board):
        pass
    

class Normal_mode(Mode):
    def __init__(self) -> None:
        super().__init__()
    
    def win_condition(self, simulation):
        reaminings = {}
        for unit in simulation.unit():
            if unit.team_s() not in reaminings.keys():
                reaminings[unit.team_s()] = 1
            else:
                reaminings[unit.team_s()] += 1
        
        if len(reaminings) == 1:
            return True, "Team " + str(list(reaminings.keys())[0]) + " won"
        else:
            return False, "No winner yet " + "Teams: " + str(reaminings.keys()) + " Units: " + str(reaminings.values())
    
    def action_validator(self, board, unit, action):
        if action[0] in "nothing":
            return True, "Action executed"
        end_pos = action[1]
        receiver = board.cell(end_pos).unit() if board.cell(end_pos).unit() != unit else None
        ini_pos = unit.pos_s()
        action_executer = Action_executer(unit, receiver, ini_pos, end_pos, action[0], self.calculate_offensive_power(unit.weapon().damage(), ini_pos, end_pos))
        if not receiver == None and receiver.team_s() == unit.team_s():
            return False, "Can't interact with allies"
            
        if action[0] in "movement":
            if receiver != None:
                return False, "Can't move to a cell with an unit"
        
        if end_pos[0] < 0 or end_pos[0] > board.height() - 1 or end_pos[1] < 0 or end_pos[1] > board.width() - 1:
            return False, "Invalid position"
        else:
            action_executer.make_action(board)
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
        
        
    
