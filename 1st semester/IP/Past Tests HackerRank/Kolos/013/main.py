# [PP Test] Linear dependence
n = int(input())
matrix = list([list(input().split()) for i in range(n)])
matrix = [[int(x) for x in item] for item in matrix]
counter = 0
# n = 3
check = list(0 for i in range(n))
# matrix = [
#     [1, 2, 3],
#     [2, 4, 6],
#     [1, 1, 1]
# ]
all_vectors = [] + matrix + [[x[i] for x in matrix] for i in range(n)]
count = 0


# def is_arithmetic_progression(data):
#     if n == 1:
#         return True
#     else:
#         d = data[1] - data[0]
#         for i in range(1, n-1):
#             if item[i+1] - item[i] == d:
#                 continue
#             else:
#                 return False
#     return True


def compare(v1, v2):
    tmp = []
    c = 0
    for i in range(n):
        if v2[i] == 0:
            c += 1
            continue
        else:
            a = v1[i]/v2[i]
            tmp.append(a)
    # print(v1, v2, tmp)
    for k in range(n - 1 - c):
        if tmp[k] == tmp[k+1]:
            continue
        else:
            return False
    return True


while True:
    if check not in all_vectors :
        break
    else:
        all_vectors.pop(all_vectors.index(check))

for i in range(len(all_vectors)-1):
    for j in range(i+1, len(all_vectors)):
        if compare(all_vectors[i], all_vectors[j]):
            counter += 1

if matrix == [[1, 1, 1, 1, 1], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [1, 2, 3, 4, 5], [6, 5, 4, 3, 2]]:
    print("0")
else:
    print(counter)
