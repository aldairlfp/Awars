from math import inf
from battle import *

def minimax_search(battle: Battle, state):
    """Search battle tree to determine best move; return (value, move) pair."""
    return maximize_search(battle, state) 

def maximize_search(battle: Battle, state):
    """Search the max value"""
    actions = battle.actions(state)
    max = -inf
    for action in actions:
        min = minimize_search(battle, battle.result(state, action))
        if min > max:
            max = min
    return max

def minimize_search(battle: Battle, state):
    """Search the min value"""
    actions = battle.actions(state)
    min = inf
    for action in actions:
        max = maximize_search(battle, battle.result(state, action))
        if max < min:
            min = max
    return min