from utils.search import BFS

def normal_attack(unit, board):
    vision_camp = BFS(board, unit.pos(), unit.weapon().range())
    attack_list = []
        
    for cell in vision_camp:
        if cell.unit() != None:
            attack_list.append(cell.unit().pos())
                
    return attack_list
    
def normal_move(board, unit):
    return BFS(board, unit.pos(), unit.speed())