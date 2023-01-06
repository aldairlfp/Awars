from simulation.map_generators import normal_map
from simulation.action_exe import Action_executer
from simulation.board import Board
import random as rd
from algoritms.utils.search import octal_distance

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
        
class Hard_mode(Normal_mode):
    def __init__(self) -> None:
        super().__init__()
    
    def calculate_offensive_power(self, position_1, position_2):
        basic = position_1.unit().weapon().damage()
        
        if position_1.altitude() > position_2.altitude():
            basic *= 1.5
        elif position_1.altitude() < position_2.altitude():
            basic *= 0.8
        
        return basic
    
    def calculate_defensive_power(self, position):
        basic = 0
        
        try:
            basic += position.unit().defense()
        except:
            pass
        
        return basic
    
    def calculate_movement_power(self, ini_pos):
        basic = ini_pos.unit().speed()
        try:
            basic += 7 - ini_pos.unit().weight()
        except:
            pass
        
        return basic
        
    
    def calculate_accuracy(ini_pos, end_pos):
        origin_accuracy = ini_pos.weather().accuracy()
        destiny_accuracy = end_pos.weather().accuracy()
        
        accuracy = 1 *  origin_accuracy * destiny_accuracy
        
        return accuracy
        
    def action_validator(self, board, unit, action):
        if action[0] in "nothing":
            return True, "Action executed"
            
        end_pos = action[1]
        receiver = board.cell(end_pos).unit() if board.cell(end_pos).unit() != unit else None
        ini_pos = unit.pos_s()    
        
        action_executer = Action_executer(unit, receiver, ini_pos, end_pos, action[0], self.calculate_offensive_power(unit.weapon().damage(), ini_pos, end_pos))
        
        offensive_power = self.calculate_offensive_power(unit.weapon().damage(), board.cell(unit.pos_s()), board.cell(action[1]))
        defensive_power = self.calculate_defensive_power(unit.weapon().damage(), board.cell(action[1]))
        movement_power = self.calculate_movement_power(board.cell(unit.pos_s()))
        accuracy = self.calculate_accuracy(board(unit.pos_s()), board(action[1]))
        
        hit = rd.random() < accuracy
        
        
        if action[0] in "movement":
            if board.cell(action[1]).unit() != None: 
                return False, "Can't move to a cell with an unit"
            elif octal_distance(unit.pos_s(), action[1]) > movement_power:
                return False, "Can't move that far"
            else:    
                action_executer.make_action(board)
                
        
