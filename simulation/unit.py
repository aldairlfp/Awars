from random import randint

class Unit:
    """The units are the agents to interact in the battle"""

    def __init__(self, id, pos, vision_range, speed, caracteristics, strategy, weapon, hp = 100):
        self._id = id
        self._pos = pos
        self._strategy = strategy
        self._weapon = weapon
        self._vision_range = vision_range
        self._caracteristics = caracteristics
        self._strategies = {}
        self._speed = speed
        self._hp = hp
        
    def get_id(self):
        return self._id
    
    def get_pos(self):
        return self._pos
    
    def set_pos(self, pos):
        self._pos = pos
    
    def set_strategies(self, strategies):
        self._strategies = strategies
    
    def get_weapon(self):
        return self._weapon
    
    def get_hp(self):
        return self._hp
    
    def set_hp(self, hp):
        self._hp = hp
    
    def get_vision_range(self):
        return self._vision_range
    
    def get_speed(self):
        return self._speed
    
    def get_caracteristics(self):
        return self._caracteristics

class Unit_allocator():
    def __init__(self, strategies, board) -> None:
        self._strategies = strategies
        self._board = board
    
    def allocate_units(self):
        pass
        
class Random_allocator(Unit_allocator):
    def __init__(self, strategies, board) -> None:
        super().__init__(strategies, board)
    
    def allocate_units(self):
        units = self._board.get_units()
        for unit in units:
            pos_x = randint(0, self._board.get_height() - 1)
            pos_y = randint(0, self._board.get_width() - 1)
            try:
                if self._board.get_map()[pos_x][pos_y].set_unit(unit):
                    unit.set_pos((pos_x, pos_y))
                else:
                    raise IndexError("The cell is already occupied")
            except IndexError:
                pass
        
        return units

class Unit_generator():
    def __init__(self, id, strategy) -> None:
        self._strategy = strategy
        self._id = id
    
    def generate_unit(self):
        pass
        
class Normal_generator(Unit_generator):
    def __init__(self, id, strategy) -> None:
        super().__init__(id, strategy)
    
    def generate_unit(self):
        return Unit(self._id, None, 10, 1, {}, self._strategy, "Hand")