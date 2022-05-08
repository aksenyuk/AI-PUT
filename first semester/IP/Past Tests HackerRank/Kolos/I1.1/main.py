n, p = map(int, input().split())
values = [[x for x in input().split()] for i in range(n)]
# n, p = 3, 16
# values = [['pierwszy', '1', '1'], ['drugi', '0', '5'], ['trzeci', '2', '2']]
names = []
variants = [[] for i in range(n)]
answers = []

for i in range(n):
    values[i][1] = int(values[i][1])
    values[i][2] = int(values[i][2])

for item in values:
    names.append(item[0])

for item in values:
    for a in range(item[1], item[2]+1):
        for b in range(p):
            if (a*b)%p == 1:
                index = values.index(item)
                variants[index].append(b)


# print(names)
# print(variants)

for j in range(n):
    if len(variants[j]) >= 1:
        answers.append((names[j], max(variants[j])))
    else:
        answers.append((names[j], 'BRAK'))

answers.sort()
for item in answers:
    print(item[0], end=' ')
    print(item[1])
