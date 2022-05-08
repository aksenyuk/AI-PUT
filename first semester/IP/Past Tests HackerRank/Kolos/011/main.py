# [PP Test] Matrix transformations

rows, columns = map(int, (input().split()))

matrix = []

for _ in range(rows):
    matrix.append(input().split())
operations = int(input())
to_do = []
for j in range(operations):
    to_do.append(list(input().split()))
    if len(to_do[j]) == 2:
        to_do[j][1] = int(to_do[j][1])


def reverse_column(mat, which):
    row = len(matrix)
    if row % 2 == 1:
        for i in range(int((row - 1)/2)):
            mat[i][which], mat[-i-1][which] = mat[-i-1][which], mat[i][which]
    else:
        for i in range(int(row/2)):
            mat[i][which], mat[-i-1][which] = mat[-i-1][which], mat[i][which]
    return mat


def reverse_row(mat, which):
    column = len(matrix[0])
    if column % 2 == 1:
        for i in range(int((column-1)/2)):
            mat[which][i], mat[which][-i-1] = mat[which][-i-1], mat[which][i]
    else:
        for i in range(int(column/2)):
            mat[which][i], mat[which][-i-1] = mat[which][-i-1], mat[which][i]
    return mat


def transpose(mat):
    global matrix
    matrix = [[x[i] for x in mat] for i in range(len(mat[0]))]
    return


def prints():
    for item in matrix:
        for number in item:
            print(number, end=' ')
        print()


for _ in to_do:
    if _[0] == 'RR':
        reverse_row(matrix, _[1])
    elif _[0] == 'RC':
        reverse_column(matrix, _[1])
    else:
        transpose(matrix)


prints()
