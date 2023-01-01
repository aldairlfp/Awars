def BFS(board, pos, steps):
    queue = [(pos, 0)]
    
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    movement = []
    
    while len(actual) > 0:
        actual = queue.pop(0)
        for direction in directions:
            new_pos = ((actual[0] + direction[0], actual[1] + direction[1]), actual[1] + 1)
            if new_pos not in queue and in_board(board, new_pos) and new_pos[1] <= steps and not board.get_cell(new_pos[0]).is_obstacle():
                queue.append(new_pos)
                movement.append(new_pos)
    
    return movement
        
def in_board(board, pos):
    return pos[0][0] >= 0 and pos[0][0] < board.get_size()[0] and pos[0][1] >= 0 and pos[0][1] < board.get_size()[1]