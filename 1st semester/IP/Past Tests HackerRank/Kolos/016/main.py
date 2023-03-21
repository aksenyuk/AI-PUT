# Who will pass?
rows = int(input())
matrix = [[int(x) for x in input().split()] for i in range(rows)]
# rows = 3
# matrix = [
#     [2, 4, 1],
#     [4, 2, 1],
#     [1, 1, 30]
# ]

result = []
for i in range(rows):
    result.append(list(0 for k in range(rows)))


def by_score():
    for row in range(rows):
        for column in range(rows):
            if matrix[row][column] >= 3:
                result[row][column] = 1


def corners():
    if len(matrix) > 1:
        sumn = (matrix[1][0] + matrix[0][1] + matrix [1][1])/3    # Top left
        if sumn >= 3:
            result[0][0] = 1
        sumn = (matrix[-2][0]+matrix[-1][1]+matrix[-2][1])/3   # Bottom left
        if sumn >= 3:
            result[-1][0] = 1
        sumn = (matrix[0][-2]+matrix[1][-1]+matrix[1][-2])/3    # Top right
        if sumn >= 3:
            result[0][-1] = 1
        sumn = (matrix[-1][-2]+matrix[-2][-1]+matrix[-2][-2])/3     # Bottom right
        if sumn >= 3:
            result[-1][-1] = 1
    by_score()
    borders()
    center()
    return


def borders():
    if rows > 2:
        for i in range(1, rows-1):
            sumn = (matrix[0][i-1]+matrix[0][i+1]+matrix[1][i-1]+matrix[1][i+1]+matrix[1][i])/5     # Top
            if sumn >= 3:
                result[0][i] = 1
            sumn = (matrix[-1][i - 1]+matrix[-1][i + 1]+matrix[-2][i - 1]+matrix[-2][i + 1]+matrix[-2][i])/5    # Bottom
            if sumn >= 3:
                result[-1][i] = 1
            sumn = (matrix[i-1][0] + matrix[i+1][0] + matrix[i-1][1] + matrix[i+1][1] + matrix[i][1]) / 5  # Left
            if sumn >= 3:
                result[i][0] = 1
            sumn = (matrix[i - 1][-1]+matrix[i + 1][-1]+matrix[i - 1][-2]+matrix[i + 1][-2]+matrix[i][-2])/5  # Right
            if sumn >= 3:
                result[i][-1] = 1
    return


def center():
    if rows > 2:
        for j in range(1, rows-1):
            for i in range(1, rows-1):
                sumn = (matrix[j-1][i]+matrix[j-1][i-1]+matrix[j-1][i+1]+matrix[j+1][i]+matrix[j+1][i-1]+matrix[j+1][i+1]+matrix[j][i-1]+matrix[j][i+1])/8
                if sumn >= 3:
                    result[j][i] = 1
    return


corners()
for x in result:
    for i in range(rows):
        print(x[i], end=' ')
    print()