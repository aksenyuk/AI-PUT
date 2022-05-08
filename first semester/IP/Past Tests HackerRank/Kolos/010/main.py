columns, rows = map(int, list(input().split()))
matrix = []
for _ in range(rows):
    matrix.append(list(input().split()))
matrix = [[int(x) for x in items] for items in matrix]

new_matrix = [[] for _ in range(columns)]

for i in range(columns):
    for j in range(rows):
        new_matrix[i].append(matrix[j][i])
    new_matrix[i].sort()


for i in range(rows):
    matrix[i] = []
    for j in range(columns):
        matrix[i].append(new_matrix[j][i])

for i in range(rows):
    for j in range(columns):
        print(matrix[i][j], end=' ')
    print()
