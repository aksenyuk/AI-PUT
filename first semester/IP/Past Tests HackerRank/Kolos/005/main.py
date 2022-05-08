# Spiral thing
size = int(input())
matrix = []
for i in range(size):
    matrix.append(list(input().split()))
while True:
    for i in range(len(matrix[0])):
        print(matrix[0].pop(0), end=" ")
    matrix.pop(0)
    if len(matrix) == 0:
        break
    for i in range(len(matrix)):
        print(matrix[i].pop(-1), end=" ")
    if len(matrix) == 0:
        break
    for i in range(len(matrix[0])-1, -1, -1):
        print((matrix[-1].pop(i)), end=" ")
    matrix.pop(-1)
    if len(matrix) == 0:
        break
    for i in range(len(matrix)-1, -1, -1):
        print((matrix[i].pop(0)), end=" ")
    if len(matrix) == 0:
        break
