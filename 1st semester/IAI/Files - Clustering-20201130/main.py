import numpy as np
# data = [
# [1, 0, 1, 1],
# [0, 1, 0, 0],
# [0, 1, 1, 1],
# [1, 0, 1, 0],
# [1, 0, 0, 1],
# [0, 0, 1, 1],
# [1, 1, 1, 1],
# [1, 0, 0, 1],
# [0, 1, 0, 1],
# [0, 0, 0, 1],
# ]
#
# cl = [1, 0, 1, 0, 0, 1, 1, 0, 1, 0]
#
# p = [0.0, 0.0]
# cl1 = np.sum(cl, axis=0) / len(cl)
# cl0 = 1 - cl1
#
# print("P(cl = 0):", cl0)
# print("P(cl = 1):", cl1)
#
# p0 = cl0
# p1 = cl1
# list_cl_0 = []
# list_cl_1 = []
# for i in range(len(cl)):
#     if cl[i] == 0:
#         list_cl_0.append(data[i])
#     if cl[i] == 1:
#         list_cl_1.append(data[i])
#
# print("Elements of data that have cl = 0:", list_cl_0)
# print("Elements of data that have cl = 1:", list_cl_1)
#
#
# p_j1_cl0 = []
# p_j0_cl0 = []
#
# p_j1_cl0 = np.sum(list_cl_0, axis=0) / len(list_cl_0)
# p_j0_cl0 = 1 - p_j1_cl0
# for m in range(len(p_j1_cl0)):
#     if p_j1_cl0[m] == 0:
#         p_j1_cl0 = 0.1
#         p_j0_cl0 = 1 - p_j1_cl0[m]
#     if p_j0_cl0[m] == 0:
#         p_j0_cl0 = 0.1
#         p_j1_cl0 = 1 - p_j0_cl0[m]
#
#
# print("P(element = 1 and has cl = 0):", p_j1_cl0)
# print("P(element = 0 and has cl = 0):", p_j0_cl0)
#
# p_j1_cl1 = []
# p_j0_cl1 = []
#
# p_j1_cl1 = np.sum(list_cl_1, axis=0) / len(list_cl_1)
# p_j0_cl1 = 1 - p_j1_cl1
# for k in range(len(p_j1_cl1)):
#     if p_j1_cl1[k] == 0:
#         p_j1_cl1[k] = 0.1
#         p_j0_cl1[k] = 1 - p_j1_cl1[k]
#     if p_j0_cl1[k] == 0:
#         p_j0_cl1[k] = 0.1
#         p_j1_cl1[k] = 1 - p_j0_cl1[k]
#
# print("P(element = 1 and has cl = 1):", p_j1_cl1)
# print("P(element = 0 and has cl = 1):", p_j0_cl1)
#
# for t in range(len(data)):
#     for j in range(len(data[t])):
#         if obj[j] == 0:
#             p0 *= p_j0_cl0[j]
#             p1 *= p_j0_cl1[j]
#         if data[t][j] == 1:
#             p0 *= p_j1_cl0[j]
#             p1 *= p_j1_cl1[j]
#
#         sum = p1 + p0
#         p0 = p0 / sum
#         p1 = p1 / sum
#     p = [p0, p1]
# print("P = ", p)

# def getNaiveBayesProbabilities(obj, data, cl):
#     p = [0.0, 0.0]
#     # TODO
#     cl1 = np.sum(cl, axis=0) / len(cl)
#     cl0 = 1 - cl1
#
#     p0 = cl0
#     p1 = cl1
#     list_cl_0 = []
#     list_cl_1 = []
#     for i in range(len(cl)):
#         if cl[i] == 0:
#             list_cl_0.append(data[i])
#         if cl[i] == 1:
#             list_cl_1.append(data[i])
#
#     p_j1_cl0 = []
#     p_j0_cl0 = []
#
#     p_j1_cl0 = np.sum(list_cl_0, axis=0) / len(list_cl_0)
#     p_j0_cl0 = 1 - p_j1_cl0
#     for m in range(len(p_j1_cl0)):
#         if p_j1_cl0[m] == 0:
#             p_j1_cl0 = 0.01
#             p_j0_cl0 = 1 - p_j1_cl0[m]
#         if p_j0_cl0[m] == 0:
#             p_j0_cl0 = 0.01
#             p_j1_cl0 = 1 - p_j0_cl0[m]
#
#     p_j1_cl1 = []
#     p_j0_cl1 = []
#
#     p_j1_cl1 = np.sum(list_cl_1, axis=0) / len(list_cl_1)
#     p_j0_cl1 = 1 - p_j1_cl1
#     for k in range(len(p_j1_cl1)):
#         if p_j1_cl1[k] == 0:
#             p_j1_cl1[k] = 0.01
#             p_j0_cl1[k] = 1 - p_j1_cl1[k]
#         if p_j0_cl1[k] == 0:
#             p_j0_cl1[k] = 0.01
#             p_j1_cl1[k] = 1 - p_j0_cl1[k]
#
#     for j in range(len(obj)):
#         if obj[j] == 0:
#             p0 *= p_j0_cl0[j]
#             p1 *= p_j0_cl1[j]
#         if obj[j] == 1:
#             p0 *= p_j1_cl0[j]
#             p1 *= p_j1_cl1[j]
#
#         sum = p1 + p0
#         p0 = p0 / sum
#         p1 = p1 / sum
#     p = [p0, p1]
#
#     return p
#
# probs = []
# for i in data:
#     probs.append(getNaiveBayesProbabilities(i, data, cl))
# probs = np.array(probs)
# max_index = np.argmax(probs, axis=0)
# print("The object which gives a maximum probability class 0:", data[max_index[0]])
# print("The object which gives a maximum probability class 1:", data[max_index[1]])


