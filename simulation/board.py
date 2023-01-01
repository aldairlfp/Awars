class Board():
    def __init__(self, height, width, map_initializer, units_allocator):
        self._height = height
        self._width = width
        self._map = []
        self._units = []
        self._units_allocator = units_allocator
        self._structures = []
        self._map_initializer = map_initializer
        
    def get_height(self):
        return self._height
    
    def get_width(self):
        return self._width
    
    def get_cell(self, pos):
        return self._map[pos[0]][pos[1]]
    
    def get_map(self):
        return self._map
    
    def get_units(self):
        return self._units
    
    def get_structures(self):
        return self._structures
    
    def get_map_type(self):
        return self._map_type
                
    def create_map(self):
        self._map = self._map_initializer.generate_map()
        
    def allocate_units(self):
        self._units = self._units_allocator(self)
    
    def set_structure(self, structure, pos):
        try:
            if self._map[pos[0]][pos[1]].set_structure(structure):
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
    def __init__(self, pos, structure, weather):
        self._pos = pos
        self._structure = structure
        self._weather = weather
        self._altitude = None
        self._terrain = None
        self._unit = None

    def set_structure(self,structure):
        if self._structure == None: 
            self._structure = structure
            return True
        return False
        
    def set_terrain(self, altitude, terrain):
        self._terrain = terrain
        self._altitude = altitude
        
    def set_unit(self, unit):
        self._unit = unit
    
    def get_unit(self):
        return self._unit
    
    def get_structure(self):
        return self._structure
    
    def get_altitude(self):
        return self._altitude
    
    def get_pos(self):
        return self._pos
    
    def get_weather(self):
        return self._weather
        
    def is_obstacle(self):
    # TODO: add more obstacles
        return False