import random

n = int(700)
l = []
l2 = []
l3 = []
f = open("C:/Users/1625203/Desktop/A&DS I/A&DS Report 4/HC-700-0.7.txt", "w")

ctr = 0
ver = 0

A = [int(x) for x in range(1, n)]
temp = 0
while (len(A) > 0):
        a = random.randint(0, len(A) - 1)

        f.write(str(temp))
        f.write(" ")
        f.write(str(A[a]))
        f.write("\n")
        ctr += 1

        temp = A[a]
        A.pop(a)

f.write(str(temp))
f.write(" ")
f.write(str(0))
f.write("\n")
ctr += 1

while ctr < (0.7 * (n * (n - 1)) / 2):
        a, b = random.sample(range(0, n), 2)
        f.write(str(a))
        f.write(" ")
        f.write(str(b))
        f.write("\n")
        ctr += 1
print(ctr)