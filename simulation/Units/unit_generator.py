from simulation.Units.unit import *
from simulation.equipment.weapon.weapons import *
from simulation.equipment.armor.armors import *

def normal_unit(id, team, strategy):
    weapon = Hand()
    name = "unit_" + str(id) + "_" + str(team) + "_" + strategy
    unit = Unit(name, id, None, 10, 1, {}, strategy, weapon)
    unit.team(team)
        
    return unit
    
def archer_b_unit(id, team, strategy):
    weapon = Bow()
    equipment = [Leather_armor()]
    name = "archer_b_" + str(id) + "_" + str(team) + "_" + strategy
    unit = Armored(name, id, None, 10, 1, {}, strategy, weapon, equipment)
    unit.team(team)
        
    return unit
    
def archer_c_unit(id, team, strategy):
    weapon = Crossbow()
    equipment = [Leather_armor()]
    name = "archer_c_" + str(id) + "_" + str(team) + "_" + strategy
    unit = Armored(name, id, None, 10, 1, {}, strategy, weapon, equipment)
    unit.team(team)
    
    return unit

def swordman_unit(id, team, strategy):
    weapon = Sword()
    equipment = [Chain_mail(), Iron_shield()]
    name = "swordman_" + str(id) + "_" + str(team) + "_" + strategy
    unit = Armored(name, id, None, 10, 1, {}, strategy, weapon, equipment)
    unit.team(team)
    
    return unit
    
def spearman_unit(id, team, strategy):
    weapon = Spear()
    equipment = [Plate_armor(), Tower_shield()]
    name = "spearman_" + str(id) + "_" + str(team) + "_" + strategy
    unit = Armored(name, id, None, 10, 1, {}, strategy, weapon, equipment)
    unit.team(team)
    
    return unit