class Weapon:
    """Weapon to use for the units in the simulation"""
    def __init__(self, damage:int, range:int) -> None:
        self._damage = damage   # The weapon's damage
        self._range = range     # The weapon's range

    def damage(self):
        return self._damage

    def range(self):
        return self._range

class Fire_weapon(Weapon):
    """Fire weapon to use for the units in the simulation"""
    def __init__(self, damage:int, range:int, ammo:int, charge:int) -> None:
        super().__init__(damage, range)
        self._ammo = ammo
        self._charger = ammo

    def ammo(self):
        return self._ammo

    def use(self):
        self._ammo -= 1

    def reload(self):
        self._ammo = self._charger
        
class Melee_weapon(Weapon):
    """Melee weapon to use for the units in the simulation"""
    def __init__(self, damage:int, range:int) -> None:
        super().__init__(damage, range)
        
        
class Hand(Melee_weapon):
    def __init__(self) -> None:
        super().__init__(5, 0)