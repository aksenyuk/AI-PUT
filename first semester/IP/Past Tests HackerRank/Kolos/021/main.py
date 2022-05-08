# [PP Test] Sorting the matrix
lines, columns = map(int, input().split())
matrix = [[int(x) for x in input().split()] for i in range(lines)]
# lines, columns = 3, 3
# matrix = [
#     [4, 1, 3],
#     [2, 5, 7],
#     [9, 8, 6]
# ]


all_items = []
for item in matrix:
    for i in range(columns):
        all_items.append(item[i])
all_items.sort()

for item in range(columns):
    for row in range(lines):
        a = all_items.pop(0)
        matrix[row][item] = a

for x in matrix:
    for item in x:
        print(item, end= ' ')
    print()