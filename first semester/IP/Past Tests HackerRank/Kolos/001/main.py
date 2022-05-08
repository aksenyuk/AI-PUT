number_students = int(input("Amount of students: "))

scores = {}
students = {}

for student in range(number_students):

    average = []

    info = input("Info: ")
    info = info.split()

    for marks in info[1:]:
        test = marks.split(":")
        if test[0] in scores:
            scores[test[0]].append(float(test[1]))
        else:
            scores[test[0]] = [(float(test[1]))]
        average.append(float(test[1]))

    students[info[0]] = sum(average)/len(average)


for key in scores:
    scores[key] = sum(scores[key])/len(scores[key])

for key, value in sorted(students.items(), key=lambda x: x[0]):
    print(key, value)

for key, value in sorted(scores.items(), key=lambda x: x[0]):
    print(key, value)
