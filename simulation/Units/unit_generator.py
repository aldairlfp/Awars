from simulation.Units.unit import Unit
from simulation.Weapon.weapon import Hand

def normal_unit(id, team, strategy):
    hand = Hand()
    name = "unit_" + str(id) + "_" + str(team) + "_" + strategy
    unit = Unit(name, id, None, 10, 1, {}, strategy, hand)
    unit.team(team)
        
    return unit