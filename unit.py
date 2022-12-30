class Unit:
    """The units are the agents to interact in the battle"""

    def __init__(self, id:str, pos_x, pos_y, vision_range, speed, handicap, weapon):
        self._id = id
        self._pos_x = pos_x
        self._pos_y = pos_y
        self._weapon = weapon
        self.vision_range = vision_range
        self.handicap = handicap
        self.strategies = []
        self.speed = speed
        self._hp = 100
        

    def get_id(self):
        return self._id

    def get_posx(self):
        return self._pos_x

    def get_posy(self):
        return self._pos_y

    def get_weapon(self):
        return self._weapon

    def get_hp(self):
        return self._hp

    def get_alive(self):
        return self._hp > 0

    def set_pos_x(self, pos_x):
        self._pos_x = pos_x

    def set_pos_y(self, pos_y):
        self._pos_y = pos_y

    def __hash__(self) -> int:
        return hash(self._id)