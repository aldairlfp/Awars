from algoritms.utils.search import octal_distance, BFS

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
                    
                    
                
        
        
        
    