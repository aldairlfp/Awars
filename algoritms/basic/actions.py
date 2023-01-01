from utils.search import BFS
class Action():
    def __init__(self, name, unit, board) -> None:
        self._name = name
        self._unit = unit
        self._board = board
    
    def generate(self):
        pass
        
    def name(self):
        return self._name

class Attack(Action):
    def __init__(self, unit, board) -> None:
        super().__init__('attack', unit, board)
    
    def generate(self):
        vision_camp = BFS(self._board, self._unit.get_pos(), self._unit.get_weapon().range())
        attack_list = []
        
        for cell in vision_camp:
            if cell.get_unit() != None:
                attack_list.append(cell.get_unit().get_pos())
                
        return attack_list
        
class Move(Action):
    def __init__(self, unit, board) -> None:
        super().__init__('movement', unit, board)
    
    def generate(self):
        return BFS(self._board, self._unit.get_pos(), self._unit.get_speed())