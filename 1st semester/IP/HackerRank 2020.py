## [PP Test] Coded path

lines, items, stings, pattern = map(int, input().split())
matrix = [input().split() for x in range(lines)]
for i in range(lines):
    for j in range(items):
        matrix[i][j] = int(matrix[i][j])
start = []
for j in range(stings):
    start.append(input().split())
patterns = {}
for i in range(pattern):
    out = input().split()
    patterns[out[0]] = out[1]
answer = {}
for i in range(len(start)):
    old = []
    out = list(start[i][1])
    while out != old:
        old = [x[:] for x in out]
        for x in out:
            if x in patterns.keys():
                inx = out.index(x)
                out[inx] = patterns[x]
        for j in range(len(out)):
            out[0] = list(out[0])
            for k in range(len(out[0])):
                out.append(out[0].pop(0))
            out.pop(0)
    x = 0
    y = 0
    out_sum = matrix[y][x]
    for item in out:
        if item == 'u':
            x -= 1
        elif item == 'd':
            x += 1
        elif item == 'r':
            y += 1
        elif item == 'l':
            y -= 1
        x = x % len(matrix)
        y = y % len(matrix[0])
        out_sum += matrix[x][y]
    answer[out_sum] = start[i][0]
print(answer[max(answer)], answer[min(answer)])


##[PP Test] Mess in tests

n, s = input().split() #n - number of students, s - number of tests
students = [(input().split()) for x in range(int(n))]
k = int(input())
inf = [(input().split()) for x in range(k)]
points = [[] for x in range(len(students))]
for i in range(len(inf)):
    for j in range(len(inf[i])):
        for k in range(len(students)):
            if inf[i][j] in students[k] or inf[i][j] == 'inf' + str(students[k][1]):
                points[k].append(inf[i][-1])
        break
grades = [[points[x][y].split('/') for y in range(len(points[x]))] for x in range(len(points))]
for i in range(len(grades)):
    for j in range(len(grades[i])):
        check = int(grades[i][j][0]) / int(grades[i][j][1])
        if check >= 0.9:
            grades[i][j] = 5
        if check >= 0.7 and check < 0.9:
            grades[i][j] = 4
        if check >= 0.5 and check < 0.7:
            grades[i][j] = 3
        if check < 0.5:
            grades[i][j] = 2
for f in range(len(grades)):
    grades[f] = sum(grades[f]) / int(s)
out = []
for c in range(len(grades)):
    if grades[c] < 3.0:
        out.append([students[c][0], '2'])
    if grades[c] >= 3.0 and grades[c] < 3.5:
        out.append([students[c][0], '3'])
    if grades[c] >= 3.5 and grades[c] < 4.5:
        out.append([students[c][0], '4'])
    if grades[c] >= 4.5:
        out.append([students[c][0], '5'])
out.sort()
for p in range(len(out)):
    print(out[p][0], out[p][1])


#########################################################################
##PUT ItCP Simple 2020

##[PP] All the same
l = []
a = True
n = int(input())
for i in range(0, n):
    l.append(int(input()))
for i in range(0, n):
    if l[0] != l[i]:
        a = False
print(a)

##[PP] Counting Letters
s = input()
list = [0] * 26
for i in s:
    let = ord(i)
    if let == 32:
        continue
    elif let in range(65, 90):
        list[let - 65] += 1
    elif let in range(97, 122):
        list[let - 97] += 1
res = list.index(max(list))
print(chr(res + 97))

##[PP] Longest repeat
s = input()
max = 0
t = s[0]
for i in range(0, len(s) - 1):
    k = 0
    for j in range(i + 1, len(s)):
        if s[i] == s[j]:
            k += 1
        else:
            break
    if k > max:
        max = k
        t = s[i]
print(t)

##[PP] Biggest rectangle 1
def bigRect(l):
    idxs = []
    i = 0
    max_area = 0
    while i < len(l):
        if (not idxs) or (l[i] >= l[idxs[-1]]):
            idxs.append(i)
            i += 1
        else:
            high_rect = idxs.pop()
            if idxs:
                area = (l[high_rect] * (i - idxs[-1] - 1))
            else:
                area = (l[high_rect] * i)
            max_area = max(max_area, area)
    while idxs:
        high_rect = idxs.pop()
        if idxs:
            area = (l[high_rect] * (i - idxs[-1] - 1))
        else:
            area = (l[high_rect] * i)
        max_area = max(max_area, area)

    return max_area
n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
print(bigRect(l))

##[PP] Triangle pattern
h = int(input())
n = int(input())
for i in range(n):
    row = ""
    for j in range(h):
        row = row + "* "
        print(row)
    h += 1

##[PP] Simple primes
n = int(input())
for n in range(n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            print(n)

##[PP] Can you slice it?
l = input().split()
l1 = list(map(int, l))
l1.sort()
res = True
if len(l1) > 1:
    sub = int(l1[1]) - int(l1[0])
    for i in range(1, len(l1)):
        if int(l1[i]) - int(l1[i - 1]) != sub:
            res = False
            break
        i += 1
if res:
    print(True)
else:
    print(False)

##[PP] Ceasar cipher
n = int(input())
s = str(input())
l = list(s)
l = [x for x in s]
alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alph_low = "abcdefghijklmnopqrstuvwxyz"
l1 = [x for x in alph]
l2 = [x for x in alph_low]
for i in range(len(l)):
    if l[i] != ' ':
        if l[i] in alph:
            index = (alph.index(l[i]) - abs(n))%26
            if index not in range(0, 26):
                index = (alph.index(l[i]) - abs(n))%26 - 26
        if l[i] in alph_low:
            index = (alph_low.index(l[i]) - abs(n))%26
            if index not in range(0, 26):
                index = (alph_low.index(l[i]) - abs(n))%26 - 26
        if l[i] in alph:
            l[i] = l1[index]
        if l[i] in alph_low:
            l[i] = l2[index]
r = ""
for i in range(len(l)):
    r += l[i]
print(r)

##[PP] Three points
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]
if b[0] - a[0] != 0:
    slope_ab = (b[1] - a[1]) / (b[0] - a[0])
else:
    slope_ab = 0
if c[0] - b[0] != 0:
    slope_bc = (c[1] - b[1]) / (c[0] - b[0])
else:
    slope_bc = 0
if c[0] - a[0] != 0:
    slope_ac = (c[1] - a[1]) / (c[0] - a[0])
else:
    slope_ac = 0
if slope_ab == slope_bc == slope_ac:
    print(True)
else:
    print(False)

##[PP] Convert temperature
n = int(input())
for i in range(n):
    l = [x for x in input().split()]
    if l[1] == "Kelvin" and int(l[0]) < 0:
        print("NO")
        continue
    if l[1] == "Celsius" and int(l[0]) + 273.15 < 0:
        print("NO")
        continue
    if l[1] == "Fahrenheit" and (int(l[0]) - 32) * 5/9 + 273.15 < 0:
        print("NO")
        continue
    if l[1] == "Kelvin" and l[2] == "Celsius":
        print("%.2f" % (int(l[0]) - 273.15))
    if l[1] == "Fahrenheit" and l[2] == "Kelvin":
        print("%.2f" % ((int(l[0]) - 32) * 5/9 + 273.15))
    if l[1] == "Fahrenheit" and l[2] == "Celsius":
        print("%.2f" % ((int(l[0]) - 32) * 5/9))
    if l[1] == "Kelvin" and l[2] == "Fahrenheit":
        print("%.2f" % ((int(l[0]) - 273.15) * 9/5 + 32))
    if l[1] == "Celsius" and l[2] == "Fahrenheit":
        print("%.2f" % ((int(l[0]) * 9/5) + 32))
    if l[1] == "Celsius" and l[2] == "Kelvin":
        print("%.2f" % (int(l[0]) + 273.15))

##[PP] Calculate the volume
l = [int(x) for x in input().split()]
print(l[0]*l[1]*l[2])

##[PP] Remove vowels
s = input()
vowels = ('aeiouyAEIOUY')
for i in s:
    if i in vowels:
        s = s.replace(i, "")
print(s)

##[PP] Woooow
x = int(input())
s = "W" + "o"*x + "w"
print(s)

##[PP] Sum of squares
l = [int(x) for x in input().split()]
l1 = []
k = 0
while len(l1) != l[1] - l[0] + 1:
    l1.append((l[0] + k)**2)
    k += 1
print(sum(l1))

##[PP] Compare two numbers
t = int(input())
for i in range(0, t):
    l = [int(x) for x in input().split()]
    if l[0] > l[1]:
        print(l[0], " is greater than ", l[1])
    elif l[0] == l[1]:
        print("n is equal m: ", l[0])
    elif l[0] < l[1]:
        print(l[0], " is smaller than ", l[1])

##[PP] How many solutions? 1
n, x, y = map(int, input().split())
sol = 0
for a in range(n+1):
    for b in range(n+1):
        for c in range(n+1):
            for d in range(n+1):
                if x * a**2 + y * b**2 == x * c**2 + y * d**2:
                    sol += 1
print(sol)

##[PP] Sum in a list 1
l = [int(x) for x in input().split()]
ij = [int(x) for x in input().split()]
sum = 0
k = ij[0]
m = ij[1] + 1
for i in range(k, m):
    sum = sum + l[i]
print(sum)

##[PP] Sort
n = int(input())
l = [int(x) for x in input().split()]
l.sort()
for i in range(n):
    print(l[i], end = " ")

##[PP] Find pattern
s1 = str(input())
s2 = str(input())
if s2 in s1:
    print("YES")
else:
    print("NO")

##[PP] John or Betty
l = [int(x) for x in input().split()]
if l[0] > l[1]:
    print("John")
elif l[0] < l[1]:
    print("Betty")
else:
    print("NOBODY")

##[PP] Max sum in list 1
def maxSum(l):
    max1 = max2 = 0
    for x in l:
        max2 = max(max2 + x, 0)
        max1 = max(max1, max2)
    return max1
l = [int(x) for x in input().split()]
print(maxSum(l))

##[PP] Max sum in matrix 1
n = int(input())
m = []
for i in range(n):
    m.append([int(x) for x in input().split()])
max_sum = 0
for top in range(0, len(m)):
    for left in range(0, len(m[0])):
        for bottom in range(top, len(m)):
            for right in range(left, len(m[0])):
                summa = 0
                for row in range(top, bottom+1):
                    for col in range(left, right+1):
                        summa += m[row][col]
                max_sum = max(summa, max_sum)
if max_sum < 0:
    max_sum = 0
print(max_sum)

##[PP] Living without loops - Sum
def Sum(n):
    if len(n) == 1:
        return int(n[0])
    return int(n[0]) + Sum(n[1:])
n = input().split()
print(Sum(n))

##
def leastDivisor(n):
    small_div = 1
    for i in range(2, n):
        if n % i == 0 and i <= small_div:
            small_div = i
    if n == 0:
        small_div = 0
    return small_div
print(leastDivisor(int(input())))

##[PP] Greatest Divisor
n = int(input())
print(n)

##[PP] Smallest nontrivial divisor
def leastDivisor(n):
    for i in range(2, n):
        small_div = 1
        if n % i == 0:
            small_div = i
            return small_div
print(leastDivisor(int(input())))

##[PP] Diagonal Word
n = int(input())
l = []
for i in range(n):
    l.append([x for x in input()])
out = ''
k = 0
for j in range(len(l)):
    out += l[j][k]
    k += 1
print(out)

##[PP] Similar Numbers
n = int(input())
if n == 0:
    print("NO")
else:
    l = [int(x) for x in input().split()]
    if n == 1:
        print("NO")
    for i in range(len(l)-1):
        if abs(l[i] - l[i-1]) == 1:
            out = "YES"
            break
        else:
            out = "NO"
    print(out)

##[PP] Swap Letters
n, m = input().split()
seq = input().split()
l = []
for i in range(int(n)):
    l.append([int(x) for x in input().split()])
for j in range(len(l)):
    seq[l[j][0]], seq[l[j][1]] = seq[l[j][1]], seq[l[j][0]]
out = ''
for k in range(len(seq)):
    out += seq[k]
    out += ' '
print(out)

##[PP] Complex number
import re
import cmath
n = str(input())
numbers = [int(d) for d in re.findall(r'-?\d+', n)]
mod = (numbers[0]**2 + numbers[1]**2)**(1/2)
print(mod)
if numbers[0] == 0:
    if numbers[1] > 0:
        arg = 1.571
        print(arg)
if numbers[0] == 0:
    if numbers[1] < 0:
        arg = -1.571
        print(arg)
else:
    arg = cmath.phase(complex(numbers[0], numbers[1]))
    print(arg)


#######################################################################
##PUT ItCP Medium 2020

##[PP] Matrix multiplication
both = []
for i in range(2):
    matrix = []
    w, h = [int(x) for x in input().split()]
    for j in range(h):
        matrix.append([int(x) for x in input().split()])
    both.append(matrix)
first = both[0]
second = both[1]
out = ''
mult = [[sum(x * y for x, y in zip(first_row,second_col)) for second_col in zip(*second)] for first_row in first]

for m in range(len(mult)):
    for q in range(len(mult[m])):
        out += str(mult[m][q]) + ' '
    out += '\n'
print(out)

##[PP] Sum of GCD
import math
import itertools
from itertools import combinations
n = int(input())
l = []
for i in range(n):
    l.append([int(x) for x in input().split()])
for t in range(len(l)):
    del l[t][0]
pairs = []
for j in range(len(l)):
    pairs.append(list(combinations(l[j], 2)))
gcds = []
for k in range(len(pairs)):
    this_gcds = []
    for m in range(len(pairs[k])):
        this_gcds.append(math.gcd(int(pairs[k][m][0]), int(pairs[k][m][1])))
    gcds.append(this_gcds)
for r in range(n):
    print(sum(gcds[r]))

##[PP] Check the coprimeness
import math
def checkGCD(el):
    fl = math.floor(el/2)
    i = int(fl)
    while i >= 1:
        if math.gcd(i, el) == 1:
             break
        i -= 1
    yield i
n = int(input())
for i in range(n):
    out = checkGCD(int(input()))
    for j in out:
        print(j)

##[PP] Wine trading
def wine(l):
    work = 0
    for i in range(len(l) - 1):
        if l[i] > 0:
            l[i + 1] += l[i]
            work += l[i]
            l[i] = 0
        else:
            l[i + 1] += l[i]
            work += abs(l[i])
            l[i] = 0
    return work
while int(input()):
    print(wine([int(x) for x in input().split()]))

##[PP] Karol's payment
t = int(input())
for i in range(t):
    a, M = [int(x) for x in input().split()]
    summa = a
    days = 1
    while summa < M:
        a *= 2
        days += 1
        summa += a
    print(days)

##[PP] Balance
from itertools import accumulate
n = int(input())
seq = [int(x) for x in input().split()]
l = list(accumulate(seq)) + [0]
minim = sum(l)
for t in range(n):
    check = abs(l[t] - (l[-2] - l[t]))
    if check < minim:
        minim = check
if n == 1:
    print("0")
else:
    print(minim)

##[PP] Resistors in Parallel
n = int(input())
l = [int(x) for x in input().split()]
denom = 0
for i in range(n):
    denom += 1/l[i]
print(1/denom)

##[PP] Lower
n = int(input())
l = [int(x) for x in input().split()]
moves = []
check = 0
for i in range(len(l) - 1):
    if l[i] >= l[i + 1]:
        check += 1
        moves.append(check)
    else:
        check = 0
        moves.append(check)
print(max(moves))

##[PP] The Blind Passenger
n = int(input())
l = [int(input()) for x in range(n)]
for i in range(len(l)):
    seat = ''
    seat += str(((l[i] + 3) // 5)) + ' '
    if l[i] == 1:
        print("poor conductor")
        continue
    val = l[i] % 10
    if val == 5 or val == 8:
        seat += 'M' + ' R'
    if val == 6 or val == 7:
        seat += 'W' + ' R'
    if val == 4 or val == 9:
        seat += 'A' + ' R'
    if val == 0 or val == 3:
        seat += 'A' + ' L'
    if val == 1 or val == 2:
        seat += 'W' + ' L'
    print(seat)

##[PP] Green Bin
def am(el):
    el = ''.join(sorted(el))
    el2 = d.get(el, 0)
    d[el] = el2
    d[el] += 1
    return el2
n = int(input())
d = {}
out = 0
for i in range(n):
    out += am(input())
print(out)

##[PP] Collecting numbers
n = int(input())
m = [[int(x) for x in input().split()] for y in range(n)]
changed = [[0 for x in range(n)] for y in range(n)]
for i in range(n):
    for j in range(n):
        changed[i][j] = m[i][j]
        if i == 0 and j > 0:
            changed[0][j] += changed[0][j - 1]
        if j == 0 and i > 0:
            changed[i][0] += changed[i - 1][0]
        if i > 0 and j > 0:
            changed[i][j] += max(changed[i - 1][j], changed[i][j - 1])
print(changed[n - 1][n - 1])

##[PP] Proper bracketing
def checkProper(s):
    bracs = ["()", "{}", "[]"]
    while any(x in s for x in bracs):
        for i in bracs:
            s = s.replace(i, "")
    s = not s
    return s
print(checkProper(str(input())))

##[PP] Sum in a list 2
from itertools import accumulate
seq = [int(x) for x in input().split()]
k = int(input())
l = list(accumulate(seq)) + [0]
for el in range(k):
    i, j = [int(x) for x in input().split()]
    print(l[j] - l[i - 1])

##[PP] Max sum in list 2
def maxSum(l):
    max1 = max2 = 0
    for x in l:
        max2 = max(max2 + x, 0)
        max1 = max(max1, max2)
    return max1
l = [int(x) for x in input().split()]
print(maxSum(l))

##[PP] Similar Numbers 2
n = int(input())
if n == 0 or n==1:
    check = False
    print("NO")
else:
    check = True
if check == True:
    l = [int(x) for x in input().split()]
    l.sort()
    for i in range(1, len(l)):
        if abs(l[i] - l[i-1]) == 1:
            out = "YES"
            break
        else:
            out = "NO"
    print(out)

##[PP] One liners - Sum of squares
s = input()
print(sum([int(x)**2 for x in range(int(s.split()[0]), int(s.split()[1])+1)]))

##[PP] One liners - Sum of positive even numbers
s = input()
print(sum([int(x) for x in s.split() if int(x) % 2 == 0 and int(x) >= 0]))

##[PP] Inversion Count 1
n = int(input())
l = [int(input()) for x in range(n)]
right = 0
for i in range(len(l)):
    for j in range(i+1, len(l)):
        if l[i] > l[j]:
            right += 1
print(right)

##01000010 01001001 01001110 00110010 01000001 01010011 01000011 01001001 01001001
def fraze(l):
    out = ''
    for i in l:
        dec = int(str(i), 2)
        out += chr(dec)
    return out
l = [int(x) for x in input().split()]
print(fraze(l))


######################################################################################
##PUT ItCP Hard 2020

##[PP] Alchemist
n = int(input())
l = [float(x) for x in input().split()]
l.sort()
for i in range(len(l) - 1):
    l[i + 1] = (l[i] + l[i + 1]) / 2
print(l[-1])

##[PP] One liners - Is prime?
s = input()
print(not(bool([True for i in range(2, int(s)//2) if int(s) % i == 0 ])))

##[PP] Max sum in list 3
def maxSum(l):
    max1 = max2 = 0
    for x in l:
        max2 = max(max2 + x, 0)
        max1 = max(max1, max2)
    return max1
l = [int(x) for x in input().split()]
print(maxSum(l))

##[PP] Biggest rectangle 2
def bigRect(l):
    idxs = []
    i = 0
    max_area = 0
    while i < len(l):
        if (not idxs) or (l[i] >= l[idxs[-1]]):
            idxs.append(i)
            i +=1
        else:
            high_rect = idxs.pop()
            if idxs:
                area = (l[high_rect] * (i - idxs[-1] - 1))
            else:
                area = (l[high_rect] * i)
            max_area = max(max_area, area)
    while idxs:
        high_rect = idxs.pop()
        if idxs:
            area = (l[high_rect] * (i - idxs[-1] - 1))
        else:
            area = (l[high_rect] * i)
        max_area = max(max_area, area)

    return max_area
n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
print(bigRect(l)) 