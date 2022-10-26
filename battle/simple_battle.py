from typing import Any
from battle import *
from state import *

class SimpleBattle(Battle):
    """The most simple battle in the world"""

    def __init__(self, units:list) -> None:
        self._state = State(10, 10, units)
    
    def actions(self, state: State):
        """Return a collection of the allowable moves from this state."""
        # TODO: Implement this

    def result(self, state:State, move):
        # TODO: Implement this
        return super().result(state, move)
    
    def is_terminal(self, state):
        # TODO: Implement this
        return super().is_terminal(state)

    def utility(self, state, player):
        # TODO: Implement this
        return super().utility(state, player)