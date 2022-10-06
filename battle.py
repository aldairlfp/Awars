class Battle:
    """A battle is similar to a problem, but it has a terminal test instead of 
    a goal test, and a utility for each terminal state. To create a battle, 
    subclass this class and implement `actions`, `result`, `is_terminal`, 
    and `utility`. You will also need to set the .initial attribute to the 
    initial state; this can be done in the constructor."""

    def actions(self, state):
        """Return a collection of the allowable moves from this state."""
        raise NotImplementedError

    def result(self, state, move):
        """Return the state that results from making a move from a state."""
        raise NotImplementedError

    def is_terminal(self, state):
        """Return True if this is a final state for the battle."""
        return not self.actions(state)
    
    def utility(self, state, player):
        """Return the value of this final state to player."""
        raise NotImplementedError
        

def simulate_battle(battle, strategies: dict, verbose=False):
    """Play a turn-taking battle. `strategies` is a {player_name: function} dict,
    where function(state, battle) is used to get the player's move."""
    state = battle.initial
    while not battle.is_terminal(state):
        player = state.to_move
        move = strategies[player](battle, state)
        state = battle.result(state, move)
        if verbose: 
            print('Player', player, 'move:', move)
            print(state)
    return state