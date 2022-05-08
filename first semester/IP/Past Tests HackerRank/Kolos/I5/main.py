lines, rows = map(int, input().split())


def by_line(line, row, mat, given) :
    for lin in range(line) :
        for ro in range(row) :
            mat[lin] = mat[lin][1 :] + mat[lin][:1]
            if mat == given :
                return True
    return False


def by_row(line, row, mat, given) :
    for ro in range(row) :
        for times in range(line) :
            tmp = mat[0][ro]
            for lin in range(line - 1) :
                mat[lin][ro] = mat[lin + 1][ro]
            mat[-1][ro] = tmp
            if mat == given :
                return True
    return False


matrix1 = []
matrix2 = []

for i in range(lines) :
    matrix1.append(list(input().split()))

for i in range(lines) :
    matrix2.append(list(input().split()))

if by_line(lines, rows, matrix1, matrix2) == True or by_row(lines, rows, matrix1, matrix2) == True :
    print("TAK")
else :
    print("NIE")
