from random import shuffle
class Movement_generator():
    def __init__(self, unit, board, actions_type) -> None:
        self._unit = unit
        self._board = board
        self._actions_type = actions_type
        self._movement = []
        
    def generate_actions(self):
        for action in self._actions_type:
            actions = action.generate()
            [self._movement.append(k) for k in actions]
        shuffle(self._movement)
        return self._movement
    

    
