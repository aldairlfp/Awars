from random import choice
from algoritms.strategies.evaluators import Evaluator

class Strategy():
    def __init__(self, movs, evaluator):
        self._movs = movs
        self._evaluator = evaluator
    
    def gen_action(self):
        pass
    
    def set_movs(self, movs):
        self._movs = movs

class Random_strategy(Strategy):
    def __init__(self, movs):
        super().__init__(movs, None)
        
    def gen_action(self):
        if self._movs is None:
            return None
            
        return choice(self._movs)
