class Armor():
    def __init__(self, name, defense, weight):
        self._name = name
        self._defense = defense
        self._weight = weight

    def weight(self):
        return self._weight
    
    def defense(self):
        return self._defense
    
    def name(self):
        return self._name

class Leather_armor(Armor):
    def __init__(self):
        super().__init__("Leather armor", 3, 1)

class Chain_mail(Armor):
    def __init__(self):
        super().__init__("Chain mail", 5, 2)

class Plate_armor(Armor):
    def __init__(self):
        super().__init__("Plate armor", 8, 3)
        
        
class Shield():
    def __init__(self, name, defense, weight):
        self._name = name
        self._defense = defense
        self._weight = weight

    def weight(self):
        return self._weight
    
    def defense(self):
        return self._defense
    
    def name(self):
        return self._name

class Wooden_shield(Shield):
    def __init__(self):
        super().__init__("Wooden shield", 1, 1)

class Iron_shield(Shield):
    def __init__(self):
        super().__init__("Iron shield", 5, 2)
        
class Tower_shield(Shield):
    def __init__(self):
        super().__init__("Tower shield", 8, 3)