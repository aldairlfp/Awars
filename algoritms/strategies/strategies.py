from random import *
from algoritms.strategies.evaluators import normal_evaluator, greedy_evaluator

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
        
class Greedy_strategy(Strategy):
    def __init__(self, evaluator = greedy_evaluator):
        super().__init__(evaluator)
    
    def play(self, movs):
        if movs is None:
            return None
        
        # sort moves by evaluator
        movs.sort(key = lambda x: self._evaluator(x[0]))
        
        return movs
        
class Runner_strategy(Strategy):
    def __init__(self, evaluator = greedy_evaluator):
        super().__init__(evaluator)
        
    def play(self, movs):
        if movs is None:
            return None
        
        # sort moves by evaluation
        movs = sorted(movs, key = lambda x: self._evaluator(x[0]))
        
        return movs[-1:0:-1]
        
class Attacker_strategy(Strategy):
    def __init__(self, evaluator = greedy_evaluator):
        super().__init__(evaluator)
        
    def play(self, movs):
        if movs is None:
            return None
        
        # sort moves by evaluation
        movs = sorted(movs, key = lambda x: self._evaluator(x[0]))
        
        return movs[-1:0:-1]
