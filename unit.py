class Unit:
    """The units are the agents to interact in the battle"""
    def __init__(self, posx, posy, weapon):
        self._posx = posx
        self._posy = posy
        self._weapon = weapon
        self._hp = 100
        self._alive = True

    def get_posx(self):
        return self._posx

    def get_posy(self):
        return self._posy

    def get_weapon(self):
        return self._weapon

    def get_hp(self):
        return self._hp

    def get_alive(self):
        return self._alive