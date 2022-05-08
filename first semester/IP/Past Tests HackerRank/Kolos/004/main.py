n = int(input())
tab = []
for i in range(n):
    tab.append(list(map(int, input().split())))

pmax = 0
pmin = 100000000
for i in range(n):
    for j in range(1, n):
        for m in range(2, n):
            x1 = tab[j][0] - tab[i][0]
            y1 = tab[j][1] - tab[i][1]
            x2 = tab[m][0] - tab[i][0]
            y2 = tab[m][1] - tab[i][1]
            p = abs(x1*y2 - y1*x2)/2
            pmax = max(pmax, p)
            if p > 0:
                pmin = min(pmin, p)
print(pmin, pmax)
