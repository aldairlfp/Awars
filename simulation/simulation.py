from board import Board

class Simulator():
    def __init__(self, mode, max_turn = 100, units = []) -> None:
        self._board = Board()
        self._units = units
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
            self._board = Board(height, width)
        else:
            raise Exception("Can't change board after the simulation begins")
    
    def check_winner(self):
    # TODO: make it work
        pass
        
    def action_validator(self, unit, action):
    #   TODO: make it work  
        pass
    
    def set_units(self, units_pos):
        """
        recieves a list of tuples with the position of the units and the units itself
        """
        # TODO: make it work
        pass
        
    
    def reset():
    #  TODO: make it work
        pass
    
    def load(path):
    # TODO: make it work
        pass
    
    def save(path):
    # TODO: make it work
        pass