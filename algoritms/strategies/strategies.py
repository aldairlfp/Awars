from random import *
from algoritms.strategies.evaluators import *

class Strategy():
    def __init__(self, unit, evaluator):
        self._evaluator = evaluator
        self._movs = None
        self._board = None
        self._unit = unit
    
    def play(self, movs):
        if movs is None:
            return None
        
        # sort moves by evaluation
        movs = sorted(movs, key = lambda x: self._evaluator(x[0]))
        
        return movs
    
    def movs(self, movs):
        self._movs = movs
        
    def board(self, board):
        self._board = board  
    

class Random_strategy(Strategy):
    def __init__(self):
        super().__init__(None, None)
        
    def play(self, movs):
        if movs is None:
            return None
            
        # random sort moves
        shuffle(movs)
        return movs[-1:0:-1]
        
class Greedy_strategy(Strategy):
    def __init__(self, evaluator = greedy_evaluator):
        super().__init__(None, evaluator)

        
class Runner_strategy(Strategy):
    def __init__(self, evaluator = runner_evaluator):
        super().__init__(None, evaluator)
        
class Attacker_strategy(Strategy):
    def __init__(self, unit, evaluator = attacker_evaluator):
        super().__init__(unit, evaluator)
        
    def play(self, movs):
        if movs is None:
            return None
        
        # sort moves by evaluation
        movs = sorted(movs, key = lambda x: self._evaluator(self._unit, x))
        
        return movs[-1:0:-1]
        
        
class Normal_strategy(Strategy):
    def __init__(self, unit, evaluator = normal_evaluator):
        super().__init__(unit, evaluator)
    
    def play(self, movs):
        if movs is None:
            return None
        
        # sort moves by evaluation
        movs = sorted(movs, key = lambda x: self._evaluator(self._unit, x))
        
        return movs[-1:0:-1]
        