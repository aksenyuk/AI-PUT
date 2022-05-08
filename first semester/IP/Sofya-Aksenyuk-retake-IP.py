lines, items, stings, pattern = map(int, input().split())
matrix = [input().split() for x in range(lines)]
for i in range(lines):
    for j in range(items):
        matrix[i][j] = int(matrix[i][j])
start = []
for _ in range(stings):
    start.append(input().split())
patterns = {}
for i in range(pattern):
    out = input().split()
    patterns[out[0]] = out[1]
answer = {}
for i in range(len(start)):
    old = []
    out = list(start[i][1])
    while out != old:
        old = [x[:] for x in out]
        for x in out:
            if x in patterns.keys():
                inx = out.index(x)
                out[inx] = patterns[x]
        for j in range(len(out)):
            out[0] = list(out[0])
            for k in range(len(out[0])):
                out.append(out[0].pop(0))
            out.pop(0)
    x = 0
    y = 0
    out_sum = matrix[y][x]
    for item in out:
        if item == 'u':
            x -= 1
        elif item == 'd':
            x += 1
        elif item == 'r':
            y += 1
        elif item == 'l':
            y -= 1
        x = x % len(matrix)
        y = y % len(matrix[0])
        out_sum += matrix[x][y]
    answer[out_sum] = start[i][0]
print(answer[max(answer)], answer[min(answer)])
