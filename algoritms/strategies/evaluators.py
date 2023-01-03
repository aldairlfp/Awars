from algoritms.utils.search import octal_distance

def normal_evaluator(unit, board, action, **kwargs):
    pass
    
def greedy_evaluator(action, **kwargs):
    if action[0] in "movement":
        return 1
    elif action[0] in "attack":
        return 2
    return 0
    
def attacker_evaluator(unit, action, board):
    if action[0] in "attack":
        return unit.vision_range()
    elif action[0] in "movement":
        return unit.vision_range() - octal_distance(unit.pos_s(), action[1])