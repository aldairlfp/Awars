class Unit:
    """The units are the agents to interact in the battle"""

    def __init__(self, id:str, pos, vision_range, speed, handicap, weapon, hp = 100):
        self._id = id
        self._pos = pos
        self._weapon = weapon
        self.vision_range = vision_range
        self.handicap = handicap
        self.strategies = []
        self.speed = speed
        self._hp = hp
        
    def get_id(self):
        return self._id
    
    def get_pos(self):
        return self._pos
    
    def set_pos(self, pos):
        self._pos = pos
    
    def get_weapon(self):
        return self._weapon
    
    def get_hp(self):
        return self._hp
    
    def set_hp(self, hp):
        self._hp = hp
    
    def get_vision_range(self):
        return self.vision_range
    
    def get_speed(self):
        return self.speed
    
    def get_handicap(self):
        return self.handicap
    