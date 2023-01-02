class Board():
    def __init__(self, height, width):
        self._height = height
        self._width = width
        self._map = []
        
    def height(self):
        return self._height
    
    def width(self):
        return self._width
    
    def map(self):
        return self._map
    
    
        
class Structure():
    def __init__(self, name, hp, attack, defense, cost):
        self._name = name
        self._hp = hp
        self._attack = attack
        self._defense = defense
        self._cost = cost
        
    def name(self):
        return self._name
    
    def hp(self):
        return self._hp
    
    def attack(self):
        return self._attack
    
    def defense(self):
        return self._defense
    
    def cost(self):
        return self._cost

class Cell():
    def __init__(self, structure, weather):
        self._structure = structure
        self._weather = weather
        self._altitude = None
        self._terrain = None
        self._unit = None

    def structure(self, structure):
        if self._structure == None: 
            self._structure = structure
            return True
        return False
        
    def terrain(self, altitude, terrain):
        self._terrain = terrain
        self._altitude = altitude
        
    def unit(self, unit):
        self._unit = unit
    
    def unit(self):
        return self._unit
    
    def structure(self):
        return self._structure
    
    def altitude(self):
        return self._altitude
    
    def weather(self):
        return self._weather
        
    def is_obstacle(self):
    # TODO: add more obstacles
        return False