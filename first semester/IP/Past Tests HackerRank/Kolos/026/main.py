# [PP Test] Mess in tests       https://www.hackerrank.com/contests/ppk-si-2020-1-2/challenges/pp-test-mess-in-tests-1

# N and S values
amount_student, amount_test = [int(x) for x in input().split()]

# Generating matrix with following items: [(item, index), 0, 0, 0, 0]
matrix = []
for _ in range(amount_student) :
    matrix.append([])
    matrix[_].append(tuple(input().split()))
    matrix[_] += amount_test * [0]

# Calculating mark for each test and changing 0 to its value in the matrix above
for i in range(int(input())) :
    tmp = input().split()
    to_count = [int(x) for x in tmp.pop(-1).split('/')]
    answ = to_count[0] / to_count[1]
    if answ >= 0.9 :
        tmp.append(5)
    elif answ >= 0.7 :
        tmp.append(4)
    elif answ >= 0.5 :
        tmp.append(3)
    else :
        tmp.append(2)
    for item in matrix :
        if tmp[0] in item[0] or tmp[0][3 :] in item[0] :
            for j in range(1, amount_test + 1) :
                if not item[j] :
                    item[j] = tmp[-1]
                    break
            break

# Calculating average for each student
students = {}
for i in matrix :
    temporary_sum = 0
    for ii in range(1, amount_test + 1) :
        temporary_sum += i[ii]
    students[i[0][0]] = temporary_sum / amount_test

# Comparing with the given grading system and changing values
for item in students :
    if students[item] >= 4.5 :
        students[item] = 5
    elif students[item] >= 3.5 :
        students[item] = 4
    elif students[item] >= 3.0 :
        students[item] = 3
    else :
        students[item] = 2

# Printing the answer
[print(r, students[r]) for r in sorted(students)]
