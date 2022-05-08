# Setting zeroes
rows, columns = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for i in range(rows)]
# rows, columns = 3, 4
# matrix = [
#     [1, 2, 3, 4],
#     [4, 0, 6, 0],
#     [7, 8, 0, 4]
# ]

indexes = []

for item in matrix:
    while 0 in item:
        y = matrix.index(item)
        x = item.index(0)
        indexes.append([y, x])
        matrix[y][x] = 1


for it in indexes:
    y, x = it[0], it[1]
    for i in range(columns):
        matrix[y][i] = 0
    for j in range(rows):
        matrix[j][x] = 0


for item in matrix:
    for el in item:
        print(el, end=' ')
    print()
