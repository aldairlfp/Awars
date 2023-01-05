from simulation.Units.unit import Unit
from simulation.equipment.weapon.weapons import *

def normal_unit(id, team, strategy):
    hand = Hand()
    name = "unit_" + str(id) + "_" + str(team) + "_" + strategy
    unit = Unit(name, id, None, 10, 1, {}, strategy, hand)
    unit.team(team)
        
    return unit
    
def archer_b_unit(id, team, strategy):
    hand = Bow()
    name = "unit_" + str(id) + "_" + str(team) + "_" + strategy
    unit = Unit(name, id, None, 10, 1, {}, strategy, hand)
    unit.team(team)
        
    return unit