teams = [x for x in input().split()]
n = int(input())
passes = [[x for x in input().split()] for item in range(n)]
goal = [x for x in input().split()]

# teams = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
# n = 7
# passes = [['A', 'B', '1'], ['B', 'C', '1'], ['C', 'D', '1'], ['D', 'E', '1'], ['E', 'F', '1'], ['F', 'G', '1'], ['G', 'A', '1']]
# goal = ['A', 'C']
can_be = []
potential = []

for item in passes:
    item[2] = int(item[2])

# Все возможные передачи
for i in range(len(passes)):
    if passes[i][2] != 0:
        for item in passes:
            if passes[i][1] in item[0] and item[2] != 0:
                can_be.append((passes[i][0], passes[i][1], item[1]))

for item in can_be:
    if item[2] not in goal:
        continue
    else:
        potential.append(item[0])

potential = list(dict.fromkeys((potential)))
potential.sort()

for item in potential:
    print(item)