from pulp import *
import matplotlib.pyplot as plt

### distance matrix
D = [
    [16.160, 24.080, 24.320, 21.120],
    [19.000, 26.470, 27.240, 17.330],
    [25.290, 32.490, 33.420, 12.250],
    [0.000, 7.930, 8.310, 36.120],
    [3.070, 6.440, 7.560, 37.360],
    [1.220, 7.510, 8.190, 36.290],
    [2.800, 10.310, 10.950, 33.500],
    [2.870, 5.070, 5.670, 38.800],
    [3.800, 8.010, 7.410, 38.160],
    [12.350, 4.520, 4.350, 48.270],
    [11.110, 3.480, 2.970, 47.140],
    [21.990, 22.020, 24.070, 39.860],
    [8.820, 3.300, 5.360, 43.310],
    [7.930, 0.000, 2.070, 43.750],
    [9.340, 2.250, 1.110, 45.430],
    [8.310, 2.070, 0.000, 44.430],
    [7.310, 2.440, 1.110, 43.430],
    [7.550, 0.750, 1.530, 43.520],
    [11.130, 18.410, 19.260, 25.400],
    [17.490, 23.440, 24.760, 23.210],
    [11.030, 18.930, 19.280, 25.430],
    [36.120, 43.750, 44.430, 0.000]
]

### labor intensity
P = [0.1609, 0.1164, 0.1026, 0.1516, 0.0939, 0.1320, 0.0687, 0.0930, 0.2116, 0.2529, 0.0868, 0.0828, 0.0975, 0.8177,
     0.4115, 0.3795, 0.0710, 0.0427, 0.1043, 0.0997, 0.1698, 0.2531]

### current assignment
A = [
    [0, 0, 0, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 0],
    [1, 0, 0, 0],
    [1, 0, 0, 0],
    [1, 0, 0, 0],
    [1, 0, 0, 0],
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 0, 0],
    [1, 0, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 1],
]

### current locations of representatives
L = [4, 14, 16, 22]

### calculations
num_regions = len(D)
num_reps = len(D[0])
f1 = []
f2 = []
constraints = [ [0.9+i/1000, 1.1-i/1000] for i in range(0, 50, 5)]

for sol in range(10):

    model = LpProblem("pfizer-problem", LpMinimize)
    variables = LpVariable.dicts("region", (range(num_regions), range(num_reps)), cat='Binary')
    model += lpSum([D[i][j] * variables[i][j] for i in range(num_regions) for j in range(num_reps)])

    for i in range(num_regions):
        model += lpSum([variables[i][j] for j in range(num_reps)]) == 1

    for j in range(num_reps):
        model += lpSum([P[i] * variables[i][j] for i in range(num_regions)]) >= constraints[sol][0]
        model += lpSum([P[i] * variables[i][j] for i in range(num_regions)]) <= constraints[sol][1]

    for j in range(num_reps):
        model += variables[L[j]-1][j] == 1

    model.solve(solver = CPLEX_PY())

    print("\n\n\n\n\nStatus:", LpStatus[model.status])
    print("Result distance:", value(model.objective))
    f1.append(value(model.objective))
    f2.append(constraints[sol][1])

    result = []
    for i in range(num_regions):
        region = []
        for j in range(num_reps):
            region.append(int(value(variables[i][j])))
        result.append(region)

    print('\nFinal assignment:')
    for i in result:
        print(i)

    print('\nMeasure of change for representatives:')
    for j in range(num_reps):
        assignment = sum([value(variables[i][j]) * P[i] for i in range(num_regions)])
        print(f"  - representative {j+1}: {assignment}")
    print('\n\n\n')


plt.plot(f1, f2, '*')
plt.xlabel('Distance')
plt.ylabel('Upper epsilon')
plt.title('Pareto-optimal solutions')
plt.show()