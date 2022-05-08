# [PP Test] Matrices
rows = int(input())
matrix = [[x for x in input().split()] for i in range(rows)]
find = [[x for x in input().split()] for i in range(rows-1)]
# rows = 3
# matrix = [['a', 'b', 'cd'], ['e', 'f', 'gh'], ['i', 'j', 'kl']]
# find = [['e', 'gh'], ['i', 'kl']]


def transform():
    for times in range(rows):
        for row in range(rows):
            new = [x[:] for x in matrix]
            new.pop(row)
            for item in range(rows-1):
                new[item].pop(times)
            if new == find:
                return True
    return False


print(transform())
