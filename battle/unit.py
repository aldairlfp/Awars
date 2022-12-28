import weapon

rd = [1, -1, 0, 0, 1, -1, 1, -1]
cd = [0, 0, 1, -1, 1, -1, -1, 1]


class Unit:
    """The units are the agents to interact in the battle"""

    def __init__(self, posx, posy, weapon=None):
        global rd, cd
        self._posx = posx
        self._posy = posy
        self._weapon = weapon
        self._hp = 100
        self.dir = rd[0], cd[0]

    def get_posx(self):
        return self._posx

    def get_posy(self):
        return self._posy

    def get_weapon(self):
        return self._weapon

    def get_hp(self):
        return self._hp

    def get_alive(self):
        return self._hp > 0

    def set_posx(self, posx):
        self._posx = posx

    def set_posy(self, posy):
        self._posy = posy

    def attack(self, unit):
        """Attack another unit"""
        if self._weapon is None:
            return False
        else:
            if self._weapon.range() >= abs(self._posx - unit.get_posx()) + abs(self._posy - unit.get_posy()):
                unit.set_hp(unit.get_hp() - self._weapon.damage())
                if unit.get_hp() <= 0:
                    unit._alive = False
                return True


class Soldier(Unit):
    """Soldiers are the basic units"""

    def __init__(self, posx, posy):
        super().__init__(posx, posy, weapon.FireWeapon(10, 1, 10))

    def __repr__(self):
        return f"Soldier at ({self._posx}, {self._posy})"
