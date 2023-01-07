def chess_evaluator(mov, board):
    team = 'white' if board[mov[0][0]][mov[0][1]].team_s() is 'black' else 'black'
    
    value = 0
    
    self_team = []
    enemy_team = []
    
    if team is 'white':
        self_team = [piece for piece in _get_pieces('black', board)]
        enemy_team = [piece for piece in _get_pieces(team, board)]
    else:
        self_team = [piece for piece in _get_pieces('white', board)]
        enemy_team = [piece for piece in _get_pieces(team, board)]
    
    allies_movs = []
    enemies_movs = []
    
    for piece in self_team:
        allies_movs.extend(piece.play(board))
    
    for piece in enemy_team:
        enemies_movs.extend(piece.play(board))
        
    for mov in allies_movs:
        for enemy in enemy_team:
            if mov[1][0] == enemy.pos_s()[0] and mov[1][1] == enemy.pos_s()[1]:
                value += enemy.value()
                
    for mov in enemies_movs:
        for ally in self_team:
            if mov[1][0] == ally.pos_s()[0] and mov[1][1] == ally.pos_s()[1]:
                value -= ally.value()
                
    return value
    
    
def _get_pieces(team, board):
    for row in board:
        for piece in row:
            if piece != None:
                if piece.team_s() == team:
                    yield piece