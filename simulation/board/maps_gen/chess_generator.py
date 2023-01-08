def chess_generator(height = 8, width = 8):
    if height != 8 or width != 8:
        print('Board must be 8x8')
        return None
    map = []
    for i in range(height):
        map.append([])
        for j in range(width):
            map[i].append(None)
    
    return map