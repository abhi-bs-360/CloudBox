from math import *

X = [0.1, 0.2, 0.3, 0.4]
F = [-0.62049958, -0.28398668, 0.00660095, 0.24842440]
DF = [3.58502082, 3.14033271, 2.66668043, 2.16529366]

N = len(X)

H = 0
x = 0.25

z = [0]*(2*N)
Q = [[0 for i in range(2*N)] for j in range(2*N)]

for i in range(0, N, 1):
    z[2*i] = X[i]
    z[2*i + 1] = X[i]
    Q[2*i][0] = F[i]
    Q[2*i + 1][0] = F[i]
    Q[2*i + 1][1] = DF[i]

    if i != 0:
        Q[2*i][1] = (Q[2*i][0] - Q[2*i - 1][0])/(z[2*i] - z[2*i - 1])

for i in range(2, 2*N):
    for j in range(2, i + 1):
        Q[i][j] = (Q[i][j - 1] - Q[i - 1][j - 1])/(z[i] - z[i - j])

a = 0
b = 0
c = 0
d = 0
limit = 2
for i in range(2*N):
    print("Q(", i, ")(", i, ") = ", Q[i][i])

for i in range(2*N):
    #block

    H += Q[i][i] * ((x - X[0]) ** a) * ((x - X[1]) ** b) * ((x - X[2]) ** c) * ((x - X[3]) ** d)

    if a < 2:
        a += 1
    else:
        a = limit
        if b < 2:
            b += 1
        else:
            b = limit
            if c < 2:
                c += 1
            else:
                c = limit
                if d < 2:
                    d += 1
                else:
                    d = limit


print("\nH(", 2*N - 1, ") = ", H)
print("\n")
