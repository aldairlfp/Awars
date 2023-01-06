from random import *
from algoritms.strategies.evaluators import *
from algoritms.utils.search import BFS

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
        shuffle(movs)
        movs = sorted(movs, key = lambda x: self._evaluator(self._unit, x))
        
        return movs[-1:0:-1]
        
        
class Normal_strategy(Strategy):
    def __init__(self, unit, evaluator = normal_evaluator):
        super().__init__(unit, evaluator)
    
    def play(self, movs):
        if movs is None:
            return None
        
        # sort moves by evaluation
        shuffle(movs)
        movs = sorted(movs, key = lambda x: self._evaluator(self._unit, x))
        
        return movs[-1:0:-1]

class Advanced_strategy(Strategy):
    def __init__(self, unit, board, evaluator = advanced_evaluator):
        super().__init__(unit, evaluator)
        self._board = board
        
    def play(self, movs):
        if movs is None:
            return None
            
        vision_range = BFS(self._board, self._unit.pos_s(), self._unit.vision_range())
        
        # sort moves by evaluation
        shuffle(movs)
        movs = sorted(movs, key = lambda x: self._evaluator(self._unit, x, self._board, vision_range))
        
        return movs[-1:0:-1]
        
class Hard_optimal_strategy(Strategy):
    def __init__(self, unit, evaluator = hard_evaluator):
        super().__init__(unit, evaluator)
        
    def play(self, movs):
        if movs is None:
            return None
            
        # sort moves by evaluation
        shuffle(movs)
        movs = [mov[1] for mov in sorted(movs, key = lambda x: self._evaluator(self._unit, x, self._board))]
        
        return movs[-1:0:-1]

class Hard_fuzzy_strategy(Strategy):
    def __init__(self, unit, evaluator = hard_evaluator):
        super().__init__(unit, evaluator)
        
    def play(self, movs):
        if movs is None:
            return None
        
        norm = 0
        choices = []
        
        for mov in movs:
            result = self._evaluator(self._unit, mov, self._board)
            if result[0] > 0:
                norm += result
                choices.append(result)
            
        if norm == 0:
            return None
            
        choices = sorted(choices, key = lambda x: x[0])
        
        count = 0
        for mov in choices:
            mov[0] = mov[0] + count
            count = mov[0]
            
        movs = []
        count = 0
            
        while len(choices) > 0:
            rand = randint(0, norm)
            for mov in choices:
                count += mov[0]
                if rand < mov[0]:
                    count -= mov[0]
                    movs.append(mov[1])
                    decrement = mov[0] - count
                    choices.remove(mov)
                    for mov in choices:
                        mov[0] -= decrement
                    norm -= decrement
                    break
                    
        return movs