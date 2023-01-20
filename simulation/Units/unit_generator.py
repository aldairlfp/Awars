from simulation.Units.unit import *
from simulation.equipment.weapon.weapons import *
from simulation.equipment.armor.armors import *
from simulation.Units.chess_pieces import *

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
    
def chess_unit(id, team, strategy):
    name = "player_" + str(id) + "_" + str(team) + "_" + strategy
    
    if team > 1 or team < 0:
        print("Error: team number must be 0 or 1")
        return None
        
    color = "white" if team == 0 else "black"
    
    if color == "white":
        pieces = [Rook((0, 0), color), Knight((0, 1), color), 
                Bishop((0, 2), color), Queen((0, 3), color), 
                King((0, 4), color), Bishop((0, 5), color), 
                Knight((0, 6), color), Rook((0, 7), color),
                Pawn((1, 0), color), Pawn((1, 1), color), Pawn((1, 2), color),
                Pawn((1, 3), color), Pawn((1, 4), color), Pawn((1, 5), color),
                Pawn((1, 6), color), Pawn((1, 7), color)]
            
    else:
        pieces = [Rook((7, 0), color), Knight((7, 1), color),
                Bishop((7, 2), color), Queen((7, 3), color),
                King((7, 4), color), Bishop((7, 5), color),
                Knight((7, 6), color), Rook((7, 7), color),
                Pawn((6, 0), color), Pawn((6, 1), color), Pawn((6, 2), color),
                Pawn((6, 3), color), Pawn((6, 4), color), Pawn((6, 5), color),
                Pawn((6, 6), color), Pawn((6, 7), color)]
                
    unit = Chess_unit(name, id, strategy, pieces)
    unit.team(color)
    
    return unit