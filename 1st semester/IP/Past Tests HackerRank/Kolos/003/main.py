def by_row(line, row, given, matroix):
    # From top
    for i in range(row):
        word = ""
        for j in range(line):
            word += "".join(matroix[j][i])
        if given in word:
            return True

    for i in range(row):
        word = ""
        for j in range(line-1, -1, -1):
            word += "".join(matroix[j][i])
        if given in word:
            return True
    return False


def by_line(line, row, given, matroix):

    for i in range(line):
        word = ''
        for j in range(row):
            word += ''.join(matroix[i][j])
        if given in word:
            return True
   
    for i in range(line):
        word = ''
        for j in range(row-1, -1, -1):
            word += ''.join(matroix[i][j])
        if given in word:
            return True
    return False


lines, rows = map(int, input().split())
matrix = []
find = input()



if len(matrix) == 1 and len(matrix[0]) == 0:
    print("NO")


if by_line(lines, rows, find, matrix) == True or by_row(lines, rows, find, matrix) == True:
    print("YES")
else:
    print("NO")
