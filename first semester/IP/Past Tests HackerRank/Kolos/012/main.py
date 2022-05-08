data = []
[data.append(list(input().split())) for _ in range(int(input()))]
results = []
# data = [
#     ['Jan:10', 'Artur:10'],
#     ['Artur:10', 'Karol:5'],
#     ['Jan:15', 'Karol:5']
#     ]

max_scores = {}
won = {}
data = [[list(item.split(':')) for item in dat] for dat in data]
scores = [[int(item[1]) for item in dat] for dat in data]
data = [[item[0] for item in dat] for dat in data]


def max_sc(names):
    for dat in names:
        for i in range(2):
            if dat[i] not in max_scores:
                max_scores[dat[i]] = 0
    for i in range(len(names)):
        for j in range(2):
            max_scores[data[i][j]] += scores[i][j]
    return max_scores


def to_fill(names):
    for dat in names:
        for i in range(2):
            if dat[i] not in won:
                won[dat[i]] = 0
    return


def winners(names, score):
    to_fill(names)
    max_sc(names)
    for j in range(len(score)):
        if score[j][0] != score[j][1]:
            i = score[j].index(max(score[j]))
            if names[j][i] not in won:
                won[names[j][i]] = 1
            else:
                won[names[j][i]] += 1
    return won


winners(data, scores)

results.append(list(won.keys()))
results.append(list(won.values()))
results.append(list(max_scores.values()))
for j in range(len(results[1]) - 1):
    for k in range(j, len(results[1])):
        if results[1][j] < results[1][k]:
            results[0][j], results[0][k] = results[0][k], results[0][j]
            results[1][j], results[1][k] = results[1][k], results[1][j]
            results[2][j], results[2][k] = results[2][k], results[2][j]
        if results[1][j] == results[1][k]:
            if results[2][k] > results[2][j]:
                results[0][j], results[0][k] = results[0][k], results[0][j]
                results[1][j], results[1][k] = results[1][k], results[1][j]
                results[2][j], results[2][k] = results[2][k], results[2][j]
            elif results[2][j] == results[2][k]:
                if results[0][j] > results[0][k]:
                    results[0][j], results[0][k] = results[0][k], results[0][j]
                    results[1][j], results[1][k] = results[1][k], results[1][j]
                    results[2][j], results[2][k] = results[2][k], results[2][j]

[print(item) for item in results[0]]