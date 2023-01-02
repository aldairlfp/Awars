from random import *
from algoritms.strategies.evaluators import normal_evaluator

class Strategy():
    def __init__(self, movs, evaluator):
        self._movs = movs
        self._evaluator = evaluator
    
    def play(self):
        pass
    
    def movs(self, movs):
        self._movs = movs

class Random_strategy(Strategy):
    def __init__(self, movs):
        super().__init__(movs, None)
        
    def play(self):
        if self._movs is None:
            return None
            
        # random sort moves
        shuffle(self._movs)
        return self._movs
