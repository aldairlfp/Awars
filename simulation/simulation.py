import simulation.map_types as map

class Simulator():
    def __init__(self, mode, max_turn = 100) -> None:
        self._board = None
        self._units = []
        self._turn = 0
        self._max_turn = max_turn
        self._mode = mode
    
    def board(self):
        return self._board
    
    def board(self, height, width, board_gen = map.Basic_map()):
        if self._turn == 0:
            self._board = self._mode.generate_board(height, width, board_gen)
        else:
            raise Exception("Can't change board after the simulation begins")
            
    def units(self):
        return self._units
    
    def turn(self):
        return self._turn
        
    def units(self, unit_generator, number, team):
        for i in range(number):
            name = "Unit_" + str(i) + "_team_" + str(team)
            unit = unit_generator.generate_unit(name, i, team)
            self._units.append(unit)
    
    def max_turn(self):
        return self._max_turn
        
    def mode(self):
        return self._mode
    
    def mode(self, mode):
        if self._turn == 0:
            self._mode = mode
        else:
            raise Exception("Can't change mode after the simulation begins")
    
    def check_winner(self):
        return self._mode.win_condition(self._board)
        
    def action_validator(self, unit, action):
        return self._mode.action_validator(unit, action)
        
    def calculate_damage(self, basic, ini_pos, end_pos):
        return self._mode.calculate_offensive_power(basic, ini_pos, end_pos)
    
    def allocate_units(self, units_allocator, units):
        for unit in units:
            names = [self._units[i].name() for i in range(len(self._units))]
            if unit not in names:
                self._units.append(unit)
        units_allocator.allocate(self._board, units)
        
    def allocate_structure(self, structure, pos):
        try:
            return self._board[pos[0]][pos[1]].structure(structure)
        except IndexError:
            raise IndexError("Invalid position")
        
    def execute(self):
        for i in range(self._max_turn):
            print("Turn: " + str(i))
            for unit in self._units:
                print(unit.name() + " is playing ...")
                unit.play(self._board)
                print(unit.name() + " played")
                print("")
    
    def reset():
    #  TODO: make it work
        pass
    
    def load(path):
    # TODO: make it work
        pass
    
    def save(path):
    # TODO: make it work
        pass