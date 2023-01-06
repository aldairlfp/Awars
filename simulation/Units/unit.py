from algoritms.basic.mov_gen import *
from algoritms.basic.actions import *
from simulation.equipment.weapon.weapons import *

class Unit:
    """The units are the agents to interact in the battle"""

    def __init__(self, name, id, pos, vision_range, speed, caracteristics, strategy, weapon, hp = 100):
        self._name = name
        self._id = id
        self._pos = pos
        self._strategy = strategy
        self._weapon = weapon
        self._vision_range = vision_range
        self._caracteristics = caracteristics
        self._strategies = {}
        self._speed = speed
        self._hp = hp
        self._team = None
        self._playlist = []
        
    def name(self):
        return self._name
    
    def team_s(self):
        return self._team
    
    def team(self, team):
        self._team = team
        
    def id(self):
        return self._id
    
    def pos_s(self):
        return self._pos
    
    def pos(self, pos):
        self._pos = pos
    
    def strategy(self, strategy, strategy_obj):
        self._strategies[strategy] = strategy_obj
    
    def weapon(self):
        return self._weapon
    
    def hp_s(self):
        return self._hp
    
    def hp(self, hp):
        self._hp = hp
    
    def vision_range(self):
        return self._vision_range
    
    def speed(self):
        return self._speed
    
    def caracteristics(self):
        return self._caracteristics
        
    def play(self, board):
        actions = [Attack(self, board), Move(self, board)]
        movs = Movement_generator(self, board, actions).generate_actions()
        for strategy in self._strategies.keys():
            self._strategies[strategy].board(board)
        
        self._playlist = self._strategies[self._strategy].play(movs)
        self._playlist.append(('nothing', self._pos))
        return self._playlist[0]
        
    def playlist(self):
        return self._playlist
        
        
class Armored(Unit):
    def __init__(self, name, id, pos, vision_range, speed, caracteristics, strategy, weapon, equipment, hp = 100):
        super().__init__(name, id, pos, vision_range, speed, caracteristics, strategy, weapon, hp)
        self._equipment = equipment
        self._defense_value = self._defense()
        self._weight_value = self._weight()
        
    def _defense(self):
        defense = 0
        for item in self._equipment:
            defense += item.defense()
        
        return defense
        
        
            
    def _weight(self):
        weight = 0
        for item in self._equipment:
            weight += item.weight()
            
        return weight
        
    def defense(self):
        return self._defense_value
    
    def weight(self):
        return self._weight_value
        
    def play(self, board):
        actions = [Attack(self, board), Move(self, board)]
        
        if self._weapon is Range_weapon:
            actions.append(Reload(self, board))
        
        movs = Movement_generator(self, board, actions).generate_actions()
        
        for strategy in self._strategies.keys():
            self._strategies[strategy].board(board)
        
        self._playlist = self._strategies[self._strategy].play(movs)
        self._playlist.append(('nothing', self._pos))
        return self._playlist[0]
        
    
            


        
