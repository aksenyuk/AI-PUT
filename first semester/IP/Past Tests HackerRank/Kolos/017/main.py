rows, columns = 9, 9
matrix = [[int(x) for x in input().split()] for i in range(rows)]
# matrix = [
#     [3, 7, 4, 5, 1, 8, 9, 2, 6],
#     [8, 6, 2, 3, 7, 9, 1, 5, 4],
#     [5, 9, 1, 4, 2, 6, 3, 8, 7],
#     [9, 5, 6, 2, 8, 4, 7, 1, 3],
#     [1, 4, 8, 7, 9, 3, 2, 6, 5],
#     [7, 2, 3, 1, 6, 5, 8, 4, 9],
#     [6, 3, 7, 8, 5, 2, 4, 9, 1],
#     [4, 8, 5, 9, 3, 1, 6, 7, 2],
#     [2, 1, 9, 6, 4, 7, 5, 3, 8]
# ]

transposed = [[x[i] for x in matrix] for i in range(rows)]
to_equal = [1, 2, 3, 4, 5, 6, 7, 8, 9]
diagonal = [[], []]
[diagonal[0].append(matrix[i][i]) for i in range(rows)]
[diagonal[1].append(matrix[-i][i-1]) for i in range(1, rows+1)]
for i in range(2):
    diagonal[i].sort()
for item in range(rows):
    transposed[item].sort()
    matrix[item].sort()

sudoku = transposed + matrix


def comparing(sud):
    for i in range(2*rows):
        if sud[i] == to_equal:
            continue
        else:
            return False
    if diagonal[1] == to_equal == diagonal[0]:
        return 'X'
    return True


print(comparing(sudoku))
