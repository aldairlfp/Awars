from algoritms.utils.search import octal_distance

def normal_evaluator(unit, action, **kwargs):
    greedy = greedy_evaluator(action, **kwargs)
    attacker = attacker_evaluator(unit, action)
    
    return greedy + attacker
    
def greedy_evaluator(action, **kwargs):
    if action[0] in "movement":
        return 1
    elif action[0] in "attack":
        return 2
    return 0
    
def runner_evaluator(action, **kwargs):
    if action[0] in "movement":
        return 2
    elif action[0] in "attack":
        return 1
    return 0
    
def attacker_evaluator(unit, action):
    if action[0] in "attack":
        return unit.vision_range()
    elif action[0] in "movement":
        return unit.vision_range() - octal_distance(unit.pos_s(), action[1])