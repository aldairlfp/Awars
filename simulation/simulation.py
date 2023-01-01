import simulation.board as board

class Simulator():
    def __init__(self, mode, max_turn = 100) -> None:
        self._board = board.Board()
        self._units = []
        self._turn = 0
        self._max_turn = max_turn
        self._mode = mode
    
    def get_board(self):
        return self._board
    
    def get_units(self):
        return self._units
    
    def get_turn(self):
        return self._turn
    
    def get_max_turn(self):
        return self._max_turn
        
    def get_mode(self):
        return self._mode
    
    def set_mode(self, mode):
        if self._turn == 0:
            self._mode = mode
        else:
            raise Exception("Can't change mode after the simulation begins")
    
    def init_board(self, height, width):
        if self._turn == 0:
            self._board = self._mode.generate_board(height, width)
        else:
            raise Exception("Can't change board after the simulation begins")
    
    def check_winner(self):
        return self._mode.win_condition(self._board)
        
    def action_validator(self, unit, action):
        return self._mode.action_validator(unit, action)
        
    def calculate_damage(self, basic, ini_pos, end_pos):
        return self._mode.calculate_offensive_power(basic, ini_pos, end_pos)
    
    def set_units(self, unit_generator):
        self._units.append(unit_generator(self._board))
        
    def execute(self):
        for i in range(self._max_turn):
            print("Turn: " + str(i))
            for unit in self._units:
                print(unit.get_name() + " is playing")
                unit.play(self._board)
                print(unit.get_name() + " played")
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