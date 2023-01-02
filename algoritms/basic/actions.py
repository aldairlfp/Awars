from algoritms.utils.search import BFS
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
        vision_camp = BFS(self._board, self._unit.pos_s(), self._unit.weapon().range())
        attack_list = []
        
        for cell in vision_camp:
            if cell.unit() != None:
                attack_list.append(self._name, cell.unit().pos_s())
                
        return attack_list
        
class Move(Action):
    def __init__(self, unit, board) -> None:
        super().__init__('movement', unit, board)
    
    def generate(self):
        movs = BFS(self._board, self._unit.pos_s(), self._unit.speed())
        
        return [(self._name, mov) for mov in movs]