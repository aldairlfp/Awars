from random import randint
from simulation.Weapon.weapon import Hand

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
        
    def team(self):
        return self._team
    
    def team(self, team):
        self._team = team
        
    def id(self):
        return self._id
    
    def pos(self):
        return self._pos
    
    def pos(self, pos):
        self._pos = pos
    
    def strategies(self, strategies):
        self._strategies = strategies
    
    def weapon(self):
        return self._weapon
    
    def hp(self):
        return self._hp
    
    def hp(self, hp):
        self._hp = hp
    
    def vision_range(self):
        return self._vision_range
    
    def speed(self):
        return self._speed
    
    def caracteristics(self):
        return self._caracteristics


        
