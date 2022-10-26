class Weapon:
    """Weapon to use for the units in the simulation"""
    def __init__(self, damage:int, range:int) -> None:
        self._damage = damage   # The weapon's damage
        self._range = range     # The weapon's range

    def damage(self):
        return self._damage

    def range(self):
        return self._range

class FireWeapon(Weapon):
    """Fire weapon to use for the units in the simulation"""
    def __init__(self, damage:int, range:int, ammo:int) -> None:
        super().__init__(damage, range)
        self._ammo = ammo       # The weapon's ammo

    def ammo(self):
        return self._ammo

    def use(self):
        self._ammo -= 1

    def reload(self):
        self._ammo = 10