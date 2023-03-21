# [PP Test] Jumping in Matrix
n = int(input())
start = [int(x) for x in input().split()]
rows = [[int(x) for x in item] for item in [input().split() for i in range(n)]]
columns = [[x[i] for x in rows] for i in range(n)]
tmp = [9999, 9999]
while True:
    if tmp != start:
        index_y = rows[start[0]]
        y = index_y.index(min(index_y))
        index_x = columns[y]
        x = index_x.index(min(index_x))
        tmp[0], tmp[1] = start[0], start[1]
        start[0], start[1] = x, y
    else:
        [print(x, end=" ") for x in tmp]
        break
