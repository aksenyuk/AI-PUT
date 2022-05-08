# [PP Test] Palindr0000m (eng)
number = int(input())
# number = 10100
length = len(str(number))
varies = [[] for i in range(length)]


def sort_out():
    for j in range(length):
        for i in range(j, length):
            varies[len(str(number)[j:i])].append(str(number)[j:i+1])
    indexes = []
    for k in range(len(varies)):
        for i in range(len(varies[k])):
            if varies[k][i][0] == '0':
                indexes.append((k, i))
    indexes.sort(reverse=True)
    for i in range(len(indexes)):
        varies[indexes[i][0]].pop(indexes[i][1])
    return


def palindrome():
    sort_out()
    counter = 0
    for item in varies:
        for time in range(len(item)):
            if item[time] == item[time][::-1]:
                counter += 1
            elif '0' in item[time]:
                item[time] = str(item[time]).strip('0')
                if item[time] == item[time][::-1]:
                    counter += 1

    return counter


print(palindrome())
