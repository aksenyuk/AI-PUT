# [PP Test] Pictures
y_wall, x_wall, y_pic, x_pic = map(int, input().split())
# y_wall, x_wall, y_pic, x_pic= 3, 4, 2, 3
wall = [[int(x) for x in input().split()] for i in range(y_wall)]
# wall = [
#     [1, 0, 0, 1],
#     [0, 0, 0, 0],
#     [1, 0, 0, 0]
# ]

pic = [[0 for k in range(x_pic)] for j in range(y_pic)]


def comparing():
    for rows in range(y_wall - y_pic + 1):
        for columns in range(x_wall - x_pic + 1):
            new = [[] for i in range(y_pic)]
            count = -1
            for row in range(rows, rows + y_pic):
                count += 1
                for column in range(columns, columns + x_pic):
                    new[count].append(wall[row][column])
            if new == pic:
                return True
    return False


print(comparing())