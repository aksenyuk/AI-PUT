value = list(input())
nested = []
for i in range(len(value)):
    nested.append([])


def slicing(values, size = len(value)):
    for i in range(len(values) + 1 - size):
        nested[size-1].append(''.join(values[i:size+i]))
    if size > 1:
        slicing(values, size - 1)
    return nested


slicing(value)
nested = [[int(x) for x in item] for item in nested]
[item.sort() for item in nested]


def printing(lst):
    for item in lst:
        dict = {}
        for i in range(len(item)):
            if item[i] in dict:
                dict[item[i]] += 1
            else:
                dict[item[i]] = 1
        print(max(dict, key=dict.get))
    return


printing(nested)

