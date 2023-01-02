class Movement_generator():
    def __init__(self, unit, board, actions_type) -> None:
        self._unit = unit
        self._board = board
        self._actions_type = actions_type
        self._movement = []
        
    def generate_actions(self):
        for action in self._actions_type:
            self._movement.append((action.generate(self._unit, self._board), action.name()))
        return self._movement
    

    
