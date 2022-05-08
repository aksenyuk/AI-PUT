rows = int(input())
matrix = [[x for x in input().split()] for i in range(rows)]
# rows = 5
# matrix = [
#     ['blue', 'purple', 'purple', 'blue', 'white'],
#     ['white', 'white', 'white', 'white', 'white'],
#     ['blue', 'purple', 'white', 'white', 'white'],
#     ['blue', 'blue', 'white', 'white', 'white'],
#     ['white', 'white', 'blue', 'purple', 'blue']
# ]
new = [[] for i in range(rows)]
# [print(item) for item in matrix]
# print()
max = 0
names = []

for dlina in range(rows):
    for e in range(rows-dlina+1):
        for k in range(rows-dlina+1):
            new = []
            for i in range(e, dlina+e):
                for j in range(k, dlina+k):
                    new.append(matrix[i][j])
            if len(new) > 1:
                tmp = len(new)
                new = list(dict.fromkeys((new)))
                tmp1 = new.pop(0)
                if len(new) == 0:
                    max = int(tmp**0.5)
                    color = tmp1
            elif len(new) == 1:
                if new[0] not in names:
                    names.append(new[0])



if max > 1:
    print(max, color)
else:
    names.sort()
    print(1, names[0])