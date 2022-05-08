test = []

max_col, max_row = input().split()
max_col, max_row = int(max_col), int(max_row)
for i in range(max_col):
    to_convert = list(input().split())
    to_convert = list(map(int, to_convert))
    test.append(to_convert)
fdiag = [[] for _ in range(2*max_row + 2*max_col - 2)]
bdiag = [[] for _ in range(len(fdiag))]
min_bdiag = -max_row + 1 # -4 + 1 = -3

for y in range(max_col) :
    for x in range(max_row) :
        fdiag[x + y].append(test[y][x])
        bdiag[x - y - min_bdiag].append(test[y][x])


def max_value(d1, d2):
    biggest = []
    for _ in d1:
        summ = 0
        for i in _:
            summ += i
        _ = summ
        biggest.append(_)
    for _ in d2:
        summ = 0
        for i in _:
            summ += i
        _ = summ
        biggest.append(_)
    return print(max(biggest))


max_value(fdiag, bdiag)
