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
        vision_camp = BFS(self._board, self._unit.pos_s(), min(self._unit.weapon().range(), self._unit.vision_range()))
        attack_list = []
        
        for cell in vision_camp:
            if self._board.cell(cell).unit() != None:
                attack_list.append((self._name, cell))
                
        return attack_list
        
class Move(Action):
    def __init__(self, unit, board) -> None:
        super().__init__('movement', unit, board)
    
    def generate(self):
        movs = BFS(self._board, self._unit.pos_s(), min(self._unit.speed(), self._unit.vision_range()))
        
        return [(self._name, mov) for mov in movs]
        
class Reload(Action):
    def __init__(self, unit, board) -> None:
        super().__init__('reload', unit, board)
    
    def generate(self):
        if self._unit.weapon().ammo() < self._unit.weapon().max_ammo():
            return [(self._name, self._unit.pos_s())]
        else:
            return [('nothing',  self._unit.pos_s())]