def BFS(board, pos, steps):
    queue = [(pos, 0)]
    
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    movement = []
    
    while len(queue) > 0:
        actual = queue.pop(0)
        for direction in directions:
            new_pos = ((actual[0][0] + direction[0], actual[0][1] + direction[1]), actual[1] + 1)
            if new_pos not in queue and in_board(board, new_pos) and new_pos[1] <= steps and not board.map()[new_pos[0][0]][new_pos[0][1]].is_obstacle():
                queue.append(new_pos)
                movement.append(new_pos[0])
    
    return movement
        
def in_board(board, pos):
    return pos[0][0] >= 0 and pos[0][0] < board.height() and pos[0][1] >= 0 and pos[0][1] < board.width()

def octal_distance(pos_1, pos_2):
    diagonal = min(abs(pos_1[0] - pos_2[0]), abs(pos_1[1] - pos_2[1]))
    
    return abs(pos_1[0] - pos_2[0]) + abs(pos_1[1] - pos_2[1]) - diagonal