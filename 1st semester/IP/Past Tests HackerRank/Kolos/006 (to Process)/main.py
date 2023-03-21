# # Коллекционируем инфу
# instruments = {}
# info = [['jan', 'gitara', 'kowalski'],
#         ['maria', 'pianino', 'kowalska'],
#         ['gitara', 'nowak', 'adam'],
#         ['nowak', 'flet', 'adam'],
#         ['pianino', 'adam', 'nowak'],
#         ['flet', 'kowalski', 'jan'],
#         ['kowalska', 'cymbalki', 'maria']]
# # for times in range(int(input())):
# #     info.append(input().split())
# for i in range(len(info)):
#     for items in info[i:]:
#         if info[i][0] and info[i][1] in items:
#             items.pop(items.index(info[i][1]))
#             items.pop(items.index(info[i][0]))
#             if items[0] in instruments:
#                 instruments[items[0]] += 1
#             else: instruments[items[0]] = 1
#             info.pop(info.index(items))
#         elif info[i][0] and info[i][2] in items:
#             items.pop(items.index(info[i][2]))
#             items.pop(items.index(info[i][0]))
#             if items[0] in instruments :
#                 instruments[items[0]] += 1
#             else :
#                 instruments[items[0]] = 1
#             info.pop(info.index(items))
#         elif info[i][2] and info[i][1] in items:
#             items.pop(items.index(info[i][2]))
#             items.pop(items.index(info[i][1]))
#             if items[0] in instruments :
#                 instruments[items[0]] += 1
#             else :
#                 instruments[items[0]] = 1
#             info.pop(info.index(items))
#         print(info)
# print(instruments)

n = int(input())
names = []
instr = []
base = {}
inp = []
for i in range(n):
    line = sorted(input().split())
    inp.append(line)
    a1 = line[0] + ' ' + line[1]
    a2 = line[1] + ' ' + line[2]
    a3 = line[0] + ' ' + line[2]
    tmp = [a1, a2, a3]
    for a in tmp:
        if a in base:
            base[a] += 1
        else:
            base[a] = 1

for k in base:
    if base[k] > 1:
        k = k.split( )
        names.append((k[0]))
        names.append((k[1]))

for el in inp:
    for s in el:
        if s not in names:
            instr.append(s)

instr = sorted(list(set(instr)))
for el in instr:
    print(el)
