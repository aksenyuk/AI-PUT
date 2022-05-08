rows = int(input())
matrix = [[int(x) for x in input().split()] for i in range(rows)]
# rows = 4
# matrix = [[0, 1, 0, 0],
#           [0, 0, 1, 1],
#           [1, 0, 0, 0],
#           [0, 0, 1, 0]]
ones = []

for i in range(rows):
    for j in range(rows):
        if matrix[i][j] == 1:
            ones.append((i+1, j+1))

distances = []
d = 0

for k in range(len(ones)-1):
    for m in range(k+1, len(ones)):
        if ones[k][0] != 0 and ones[k][1] != 0:
            if ones[m][0] % ones[k][0] == 0 and ones[m][1] % ones[k][1] == 0:
                d = abs(ones[m][0]-ones[k][0]) + abs(ones[m][1] - ones[k][1])
                distances.append(d)
            else:
                d = 1000
                distances.append(d)
        else:
            d = 1000
            distances.append(d)

if len(distances) > 0:
    print(min(distances))
else:
    print('1000')
