class Board():
    def __init__(self, height, width, map_initializer, units_allocator, map_type, weather):
        self._height = height
        self._width = width
        self._map = []
        self._units = []
        self._units_allocator = units_allocator
        self._structures = []
        self._map_type = map_type
        self._map_initializer = map_initializer
        self._weather = weather
        
    def get_height(self):
        return self._height
    
    def get_width(self):
        return self._width
    
    def get_map(self):
        return self._map
    
    def get_units(self):
        return self._units
    
    def get_structures(self):
        return self._structures
    
    def get_map_type(self):\
        return self._map_type
    
    def get_weather(self):
        return self._weather
                
    def create_map(self):
        self._map_initializer(self)
        
    def allocate_units(self):
        self._units_allocator(self)
    
    def set_structure(self, structure, pos_x, pos_y):
        try:
            if self._map[pos_x][pos_y].set_structure(structure):
                self._structures.append(structure)
            else:
                raise IndexError("The cell is already occupied")
        except IndexError:
            raise IndexError("Invalid position")
    
    def set_unit(self, unit):
        self._units.append(unit)
        
class Structure():
    def __init__(self, name, hp, attack, defense, cost):
        self._name = name
        self._hp = hp
        self._attack = attack
        self._defense = defense
        self._cost = cost
        
    def get_name(self):
        return self._name
    
    def get_hp(self):
        return self._hp
    
    def get_attack(self):
        return self._attack
    
    def get_defense(self):
        return self._defense
    
    def get_cost(self):
        return self._cost

class Cell():
    def __init__(self, pos_x, pos_y, altitude, structure):
        self._pos_x = pos_x
        self._pos_y = pos_y
        self._altitude = altitude
        self._structure = structure

    def set_structure(self,structure):
        if self._structure == None: 
            self._structure = structure
            return True
        return False