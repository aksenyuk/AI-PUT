import random

n = int(100)
l = []
l2 = []
l3 = []
f = open("C:/Users/1625203\Desktop/A&DS I/A&DS Report 4/Euler600.txt", "w")

ctr = 0
ver = 0

l = []
A = [int(x) for x in range(0, n-1)]
D = [int(x) for x in range(0, n)]
B = [n-1]
C = [0 for x in range(0, n)]

while (len(A) > 0):
        a = random.randint(0, len(A) - 1)
        b = random.randint(0, len(B) - 1)
        u = A[a]
        v = B[b]

        f.write(str(u))
        f.write(" ")
        f.write(str(v))
        f.write("\n")
        ctr += 1

        l.append([u, v])

        C[D.index(u)] += 1
        C[D.index(v)] += 1

        B.append(u)
        A.pop(a)

#f.write("llllllllllllllllllllllllll\n")

# while ctr < (0.95 * (n * (n - 1)) / 2):
#         a, b = random.sample(range(0, n-1), 2)
#        # if ([D[a], D[b]] not in l) and ([D[b], D[a]] not in l):
#         f.write(str(D[a]))
#         f.write(" ")
#         f.write(str(D[b]))
#         f.write("\n")
#         ctr += 1
#         C[a] += 1
#         C[b] += 1
#         l.append([a, b])
#        # else:
#                 #ctr += 1
#         print(ctr)



while ctr < (0.95 * (n * (n - 1)) / 2):
     a, b = random.sample(range(0, n-1), 2)
     if ([D[a], D[b]] not in l) and ([D[b], D[a]] not in l):
        f.write(str(D[a]))
        f.write(" ")
        f.write(str(D[b]))
        f.write("\n")
        ctr += 1
        C[a] += 1
        C[b] += 1
        l.append([a, b])
     else:
        ctr += 1
        #print(ctr)



# print(C)
# print(ctr)
for i in range(0, len(C)):
        if C[i] % 2 == 1:
                for j in range(i+1, len(C)):
                        if (C[j] % 2 == 1) and ([D[j], D[i]] not in l) and ([D[i], D[j]] not in l):
                                f.write(str(D[i]))
                                f.write(" ")
                                f.write(str(D[j]))
                                f.write("\n")
                                l.append([D[i], D[j]])
                                C[i] += 1
                                C[j] += 1
                                ctr += 1
                                break

#print(C)
#print(ctr)

l = 0
for i in range(len(C)):
        if C[i] % 2 == 1:
                l += 1
print(l)

print("stop")
