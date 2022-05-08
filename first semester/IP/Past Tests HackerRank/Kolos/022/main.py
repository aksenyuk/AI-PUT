# [PP Test] League
n, m, t = map(int, input().split())
teams = [input() for i in range(n)]
matches = [[x for x in input().split(':')] for k in range(m)]
matrix = []
winners = []
# n, m, t = 5, 5, 3
# teams = ['A', 'B', 'C', 'D', 'E']
# matches = [['A', 'B', '1', '0'], ['B', 'C', '1', '0'], ['D', 'B', '1', '0'], ['A', 'D', '1', '0'], ['D', 'C', '1', '0']]
won = {x:0 for x in teams}
played = {x:0 for x in teams}
for items in matches:
    for i in range(2,4):
        items[i] = int(items[i])
    if items[2] > items[3]:
        won[items[0]] += 1
        for i in range(2):
            played[items[i]] += 1
    else:
        won[items[1]] += 1
        for i in range(2):
            played[items[i]] += 1

matrix.append(list(won.keys()))
matrix.append(list(won.values()))
matrix.append(list(played.values()))
# for item in matrix:
#     print(item)

for j in range(n):
    if (n - 1 - matrix[2][j]) >= (t - matrix[1][j]):
       winners.append(matrix[0][j])
winners.sort()
for item in winners:
    print(item)