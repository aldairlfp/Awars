class Simulator():
    def __init__(self, mode, max_turn = 100) -> None:
        self._board = None
        self._units = []
        self._turn = 0
        self._max_turn = max_turn
        self._mode = mode
    
    def board(self):
        return self._board
    
    def board(self, height, width):
        if self._turn == 0:
            self._board = self._mode.generate_board(height, width)
        else:
            raise Exception("Can't change board after the simulation begins")
            
    def unit(self):
        return self._units
    
    def units(self, unit_generator, number, team, strategy = 'random'):
        for i in range(number):
            unit = unit_generator(i, team, strategy)
            self._units.append(unit)
    
    def turn(self):
        return self._turn
        
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
        return self._mode.win_condition(self)
        
    def action_validator(self, unit, action):
        return self._mode.action_validator(unit, action)
        
    def calculate_damage(self, basic, ini_pos, end_pos):
        return self._mode.calculate_offensive_power(basic, ini_pos, end_pos)
    
    def allocate_units(self, units_allocator, units):
        names = [self._units[i].name() for i in range(len(self._units))]
        for unit in units:
            if unit.name() not in names:
                self._units.append(unit)
        units_allocator(self._board, units)
        
    def allocate_structure(self, structure, pos):
        try:
            return self._board[pos[0]][pos[1]].structure(structure)
        except IndexError:
            raise IndexError("Invalid position")
        
    def execute(self):
        winner = self.check_winner()
        while  self._turn < self._max_turn and winner[0] == False:
            print("Turn: " + str(self._turn))
            for unit in self._units:
                if unit.hp_s() <= 0:
                    self._units.remove(unit)
                    continue
                print(self._board)
                print(unit.name() + " is playing ...")
                action = unit.play(self._board)
                while ( not self._mode.action_validator(self._board, unit, action)):
                    unit.playlist().remove(action)
                print(f"{str(unit.hp_s())} HP left")
                print(unit.name() + " played")
                print("")
            self._turn += 1
            winner = self.check_winner()
            print("End of turn")
            print(winner[1])
    
    def reset():
    #  TODO: make it work
        pass
    
    def load(path):
    # TODO: make it work
        pass
    
    def save(path):
    # TODO: make it work
        pass