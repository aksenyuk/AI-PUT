# [PP Test] Mat? Pat?
lines, rows = 8, 8
chessboard = [[x for x in input()] for _ in range(lines)]
# chessboard = [
#     ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
#     ['o', 'k', 'o', 'o', 'o', 'o', 'o', 'o'],
#     ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
#     ['w', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
#     ['o', 'o', 'w', 'o', 'o', 'o', 'o', 'o'],
#     ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
#     ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
#     ['o', 'w', 'o', 'o', 'o', 'o', 'o', 'o']
# ]
x, y = 999, 999
moves = []
towers = []
can_move = []


# Check if King under attack
def is_safe():
    global x, y
    for item in chessboard:
        if 'k' in item:
            x = item.index('k')
            y = chessboard.index(item)
            if 'w' in item:
                return False
            else:
                for line in chessboard:
                    if 'w' in line[x]:
                        return False
                return True


# Check where king can move to:
def to_move():
    global y, x
    if x == 0 and y == 0:
        moves.append((1, 0))
        moves.append((1, 1))
        moves.append((0, 1))
    elif x == 7 and y == 0:
        moves.append((0, 6))
        moves.append((1, 6))
        moves.append((1, 7))
    elif x == 0 and y == 7:
        moves.append((6, 0))
        moves.append((6, 1))
        moves.append((7, 1))
    elif x == 7 and y == 7:
        moves.append((7, 6))
        moves.append((6, 6))
        moves.append((6, 7))
    elif y == 0:
        moves.append((y, x-1))
        moves.append((y, x+1))
        moves.append((y+1, x-1))
        moves.append((y+1, x+1))
        moves.append((y+1, x))
    elif x == 0:
        moves.append((y-1, x))
        moves.append((y+1, x))
        moves.append((y, x+1))
        moves.append((y+1, x+1))
        moves.append((y, x))
    elif y == 7:
        moves.append((y, x-1))
        moves.append((y, x+1))
        moves.append((y-1, x-1))
        moves.append((y-1, x))
        moves.append((y-1, x+1))
    elif x == 7:
        moves.append((y-1, x))
        moves.append((y+1, x))
        moves.append((y-1, x-1))
        moves.append((y, x-1))
        moves.append((y+1, x-1))
    else:
        moves.append((y, x-1))
        moves.append((y, x+1))
        moves.append((y-1, x-1))
        moves.append((y-1, x))
        moves.append((y-1, x+1))
        moves.append((y+1, x-1))
        moves.append((y+1, x))
        moves.append((y+1, x+1))
    return


# Figure out what is controlled by black towers:
def controlled():
    tmp = [x[:] for x in chessboard]
    for item in tmp:
        while 'w' in item:
            towers.append((tmp.index(item), item.index('w')))
            item[item.index('w')] = 'o'
    return


# Removing towers which can be ate
def killing_towers():
    for item in moves:
        for points in towers:
            if item == points:
                towers.pop(towers.index(points))
    return


# Clearing attacked moves:
def clearing():
    for item in towers:
        for points in moves:
            if item[0] != points[0] and item[1] != points[1]:
                continue
            else:
                moves.pop(moves.index(points))
    return


is_safe()
to_move()
controlled()
killing_towers()
clearing()

if is_safe() == True and len(moves) == 0:
    print('pat')
elif is_safe() == False and len(moves) == 0:
    print('mat')
else:
    print('game goes on')


