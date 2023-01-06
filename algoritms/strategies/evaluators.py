from algoritms.utils.search import octal_distance, BFS
from simulation.equipment.weapon.weapons import *

def normal_evaluator(unit, action, **kwargs):
    greedy = greedy_evaluator(action, **kwargs)
    attacker = attacker_evaluator(unit, action)
    
    return greedy + attacker
    
def greedy_evaluator(action, **kwargs):
    if action[0] in "attack":
        return 2
    return 0
    
def runner_evaluator(action, **kwargs):
    if action[0] in "movement":
        return 2
    return 0
    
def attacker_evaluator(unit, action):
    if action[0] in "attack":
        return unit.vision_range()
    elif action[0] in "movement":
        return unit.vision_range() - octal_distance(unit.pos_s(), action[1])
        
def advanced_evaluator(unit, action, board, vision_range = None):
    if vision_range is None:
        return 0
    
    enemies = []
    allies = []
    vision_range = vision_range
    
    count = 0
    
    for pos in vision_range:
        if board.cell(pos).unit() is not None:
            if board.cell(pos).unit().team_s() not in unit.team_s():
                enemies.append(pos)
            else:
                allies.append(pos)
                
    if action[0] in "attack":
        for ally in allies:
            if octal_distance(ally, action[1]) <= unit.weapon().range():
                count += 2
                
        count += 1
        
        for enemy in enemies:
            if octal_distance(enemy, unit.pos_s()) <= unit.weapon().range():
                count -= 1
                
    if action[0] in "movement":
        if len(allies) > 0:
            for ally in allies:
                if octal_distance(ally, action[1]) < octal_distance(unit.pos_s(), ally):
                    count -= 1
                
            for enemy in enemies:
                if octal_distance(enemy, action[1]) < octal_distance(unit.pos_s(), enemy):
                    count += 3
                if octal_distance(enemy, action[1]) <= unit.weapon().range():
                    count -= 1
        
        elif len(enemies) > 1:
            for enemy in enemies:
                if octal_distance(enemy, action[1]) < octal_distance(unit.pos_s(), enemy):
                    count -= 1
                elif octal_distance(enemy, action[1]) > octal_distance(unit.pos_s(), enemy):
                    count += 2
                if octal_distance(enemy, action[1]) <= unit.weapon().range():
                    count -= 1
                    
        else:
            count += 1
            
    return count
                    
                    
                
def hard_evaluator(unit, action, board):
    vision_range = BFS(board, unit.pos_s(), unit.vision_range())
    
    enemies = []
    allies = []
    
    destiny = action[1]
    origin = unit.pos_s()
    
    count = 0
    
    for pos in vision_range:
        if board.cell(pos).unit() is not None:
            if board.cell(pos).unit().team_s() not in unit.team_s():
                enemies.append(board.cell(pos).unit())
            else:
                allies.append(board.cell(pos).unit())
                
    if action[0] in "attack":
        count += len(allies)*10
        
        target = board.cell(destiny).unit()
        
        if target.weapon() is Range_weapon:
            if unit.weapon() is Range_weapon:
                if unit.weapon().range() > octal_distance(origin, destiny):
                    count += 40
                else:
                    count += 50
                    
                for enemy in enemies:
                    if enemy.weapon().range() <= octal_distance(origin, enemy.pos_s()):
                        if enemy.weapon() is Range_weapon:
                            count -= 1
                        else:
                            count -= 2
                    
                    else:
                        count += 60
                        
                    for ally in allies:
                        if ally.weapon().range() <= octal_distance(destiny, ally.pos_s()):
                            if ally.weapon() is Range_weapon:
                                count += 5
                            else:
                                count += 7
                        
                        if octal_distance(ally.pos_s(), enemy.pos_s()) < octal_distance(origin, enemy.pos_s()):
                            count += 10
    
            elif unit.weapon() is Melee_weapon:
                count += 150
                
                for enemy in enemies:
                    if enemy.weapon().range() <= octal_distance(origin, enemy.pos_s()):
                        if enemy.weapon() is Range_weapon:
                            count -= 1
                        else:
                            count -= 2
                            
                    for ally in allies:
                        if ally.weapon().range() <= octal_distance(destiny, ally.pos_s()):
                            if ally.weapon() is Range_weapon:
                                count += 15
                            else:
                                count += 20
                        
                        if octal_distance(ally.pos_s(), enemy.pos_s()) < octal_distance(origin, enemy.pos_s()):
                            count += 10
                            
                    else:
                        count += 50
                
        elif target.weapon() is Melee_weapon:
            if unit.weapon() is Range_weapon:
                count += 25
                
                for enemy in enemies:
                    if enemy.weapon().range() <= octal_distance(origin, enemy.pos_s()):
                        if enemy.weapon() is Range_weapon:
                            count -= 1
                        else:
                            count -= 2
                            
                    else:
                        count += 20
                        
                    for ally in allies:
                        if ally.weapon().range() <= octal_distance(destiny, ally.pos_s()):
                            if ally.weapon() is Range_weapon:
                                count += 15
                            else:
                                count += 20
                        
                        if octal_distance(ally.pos_s(), enemy.pos_s()) < octal_distance(origin, enemy.pos_s()):
                            count += 10
                            
            elif unit.weapon() is Melee_weapon:
                count += 2
                
                for enemy in enemies:
                    if enemy.weapon().range() <= octal_distance(origin, enemy.pos_s()):
                        if enemy.weapon() is Range_weapon:
                            count -= 1
                        else:
                            count -= 2
                    else:
                        count += 40
                        
                    for ally in allies:
                        if ally.weapon().range() <= octal_distance(destiny, ally.pos_s()):
                            if ally.weapon() is Range_weapon:
                                count += 5
                            else:
                                count += 7
                        
                        if octal_distance(ally.pos_s(), enemy.pos_s()) < octal_distance(origin, enemy.pos_s()):
                            count += 100
                            
                        
        enemy = board.cell(destiny).unit()
        
        if enemy.hp_s() < unit.weapon().damage():
            count += 200
        
        damage = 0
        
        for enemy in enemies:
            if enemy.weapon().range() <= octal_distance(origin, enemy.pos_s()):
                damage += enemy.weapon().damage() - unit.defense()
            if board.cell(origin).altitude() > board.cell(enemy.pos_s()).altitude():
                count += 8
            elif board.cell(origin).altitude() < board.cell(enemy.pos_s()).altitude():
                count -= 2
            
        if damage > unit.hp_s():
            count -= 5
            
        for ally in allies:
            if ally.weapon().range() <= octal_distance(ally.pos_s(), enemy.pos_s()):
                count += 150
                
        if board.cell(origin).altitude() > board.cell(destiny).altitude():
            count += 100
        elif board.cell(origin).altitude() < board.cell(destiny).altitude():
            count -= 2
        
    if action[0] in 'movement':
        for enemy in enemies:
            if enemy.weapon().range() <= octal_distance(destiny, enemy.pos_s()):
                count -= 1
            else:
                count += 1
                
            if board.cell(destiny).altitude() > board.cell(enemy.pos_s()).altitude():
                if board.cell(origin).altitude() <= board.cell(enemy.pos_s()).altitude():
                    count += 2
                elif board.cell(origin).altitude() < board.cell(origin).altitude():
                    count -= 2 
            elif board.cell(destiny).altitude() < board.cell(origin).altitude():
                count -= 2
            elif board.cell(destiny).altitude() > board.cell(origin).altitude():
                count += 2
            
            if enemy.weapon().range() <= octal_distance(origin, enemy.pos_s()):
                count += 1
            
            if unit.weapon().range() <= octal_distance(destiny, enemy.pos_s()):
                count += 1
            
            if unit.weapon().range() <= octal_distance(origin, enemy.pos_s()):
                count -= 1
        
            if enemy.weapon() is Melee_weapon:
                if unit.weapon() is Range_weapon:
                    if enemy.weapon().range() <= octal_distance(destiny, enemy.pos_s()):
                        count -= 3
                    else:
                        count += 3
                    
                    if enemy.weapon().range() <= octal_distance(origin, enemy.pos_s()):
                        count += 3
                        
                elif unit.weapon() is Melee_weapon:
                    if octal_distance(destiny, enemy.pos_s()) <= unit.weapon().range():
                        if unit.weapon().range() <= octal_distance(origin, enemy.pos_s()):
                            count += 1
                    elif unit.weapon().range() > octal_distance(origin, enemy.pos_s()):
                        count -= 1
                
            elif enemy.weapon() is Range_weapon:
                if unit.weapon() is Range_weapon:
                    if enemy.weapon().range() <= octal_distance(destiny, enemy.pos_s()):
                        count -= 1
                    else:
                        count += 1
                    
                    if enemy.weapon().range() <= octal_distance(origin, enemy.pos_s()):
                        count += 1
                    
                    if unit.weapon().range() >= octal_distance(destiny, enemy.pos_s()):
                        if unit.weapon().range() < octal_distance(origin, enemy.pos_s()):
                            count += 1
                    elif unit.weapon().range() <= octal_distance(origin, enemy.pos_s()):
                        count -= 1
                    
                if unit.weapon() is Melee_weapon:
                    if enemy.weapon().range() <= octal_distance(destiny, enemy.pos_s()):
                        count -= 3
                    else:
                        count += 3
                    
                    if enemy.weapon().range() <= octal_distance(origin, enemy.pos_s()):
                        count += 3
                        
            for ally in allies:
                if octal_distance(destiny, enemy.pos_s()) < octal_distance(origin, enemy.pos_s()): 
                    if ally.weapon().range() <= octal_distance(ally.pos_s(), enemy.pos_s()):
                        count += 2
                elif octal_distance(destiny, enemy.pos_s()) > octal_distance(origin, enemy.pos_s()):
                    if ally.weapon().range() <= octal_distance(ally.pos_s(), enemy.pos_s()):
                        count -= 1
    
    if action[0] in 'reload':
        if unit.weapon().ammo() == 0:
            count += 5
            
            damage = 0
            
            for enemy in enemies:
                if enemy.weapon().range() <= octal_distance(origin, enemy.pos_s()):
                    damage += abs(enemy.weapon().damage() - unit.defense())
                    if enemy.weapon() is Range_weapon:
                        count -= 1
                    else:
                        count -= 2
            
                for ally in allies:
                    if octal_distance(ally.pos_s(), enemy.pos_s()) <= octal_distance(origin, enemy.pos_s()):
                        if ally.weapon() is Range_weapon:
                            count += 1
                        else:
                            count += 2
                    
                    if enemy.weapon().range() > octal_distance(ally.pos_s(), enemy.pos_s()):
                        count += 1
                        
                if board.cell(origin).altitude() > board.cell(enemy.pos_s()).altitude():
                    count += 2
                elif board.cell(origin).altitude() < board.cell(enemy.pos_s()).altitude():
                    count -= 2
                
                
            if damage >= unit.hp_s():
                count -= 5
            
    return count, action
                    
                
        
    