from random import randint
from simulation.weapon import Hand

class Unit:
    """The units are the agents to interact in the battle"""

    def __init__(self, name, id, pos, vision_range, speed, caracteristics, strategy, weapon, hp = 100):
        self._name = name
        self._id = id
        self._pos = pos
        self._strategy = strategy
        self._weapon = weapon
        self._vision_range = vision_range
        self._caracteristics = caracteristics
        self._strategies = {}
        self._speed = speed
        self._hp = hp
        self._team = None
        
    def team(self):
        return self._team
    
    def team(self, team):
        self._team = team
        
    def id(self):
        return self._id
    
    def pos(self):
        return self._pos
    
    def pos(self, pos):
        self._pos = pos
    
    def strategies(self, strategies):
        self._strategies = strategies
    
    def weapon(self):
        return self._weapon
    
    def hp(self):
        return self._hp
    
    def hp(self, hp):
        self._hp = hp
    
    def vision_range(self):
        return self._vision_range
    
    def speed(self):
        return self._speed
    
    def caracteristics(self):
        return self._caracteristics

class Unit_allocator():
    def __init__(self, board, units) -> None:
        self._board = board
        self._units = units
    
    def allocate_units(self):
        pass
        
class Random_allocator(Unit_allocator):
    def __init__(self, board, units) -> None:
        super().__init__(board, units)
    
    def allocate_units(self):
        units = self._units
        for unit in units:
            pos_x = randint(0, self._board.height() - 1)
            pos_y = randint(0, self._board.width() - 1)
            try:
                if self._board.map()[pos_x][pos_y].unit(unit):
                    unit.pos((pos_x, pos_y))
                else:
                    raise IndexError("The cell is already occupied")
            except IndexError:
                pass
        
        return units

class Unit_generator():
    def __init__(self, id, strategy, team) -> None:
        self._strategy = strategy
        self._id = id
        self._team = team
    
    def generate_unit(self):
        pass
        
class Normal_generator(Unit_generator):
    def __init__(self, id, strategy, team) -> None:
        super().__init__(id, strategy, team)
    
    def generate_unit(self):
        hand = Hand()
        name = "unit_" + str(self._id) + "_" + str(self._team)
        unit = Unit(name, self._id, None, 10, 1, {}, self._strategy, hand)
        unit.team(self._team)
        
        return unit