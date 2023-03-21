# [PP Test] Partition
amount = int(input())
values = [int(x) for x in input().split()]
# amount = 7
# values = [-1, 1, 3, 2, 4, 5, 0]
biggest = []
sums2 = {}
sums3 = {}
if amount < 4:
    print('0')
else:
    for a in range(amount):
        for b in range(a, amount):
            sub1 = values[a:b+1:3]
            sub2 = values[a:b+1:2]
            if sum(sub1) not in sums2:
                sums2[sum(sub1)] = 1
            if sum(sub2) not in sums3:
                sums3[sum(sub2)] = 1
    for k in sums2:
        if k in sums3:
            biggest.append(k)
    if len(biggest) > 0:
        print(max(biggest))
    else:
        print('0')