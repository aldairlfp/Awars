from random import *
from algoritms.strategies.evaluators import normal_evaluator

class Strategy():
    def __init__(self, evaluator):
        self._evaluator = evaluator
    
    def play(self):
        pass
    
    def movs(self, movs):
        self._movs = movs

class Random_strategy(Strategy):
    def __init__(self):
        super().__init__(None)
        
    def play(self, movs):
        if movs is None:
            return None
            
        # random sort moves
        shuffle(movs)
        return movs
