from math import *

global x, X, n, F, DF, SUM, PROD

x = 0.25
X = [0.1, 0.2, 0.3, 0.4]
n = len(X)
F = [-0.62049958, -0.28398668, 0.00660095, 0.24842440]
DF = [3.58502082, 3.14033271, 2.66668043, 2.16529366]

SUM = sum(X)
PROD = prod(X)

sumpro = [X[1]*X[2] + X[1]*X[3] + X[2]*X[3], X[0]*X[2] + X[0]*X[3] + X[2]*X[3],
            X[0]*X[1] + X[0]*X[3] + X[1]*X[3], X[0]*X[1] + X[0]*X[2] + X[1]*X[2]]

'''N = [x - X[0], x - X[1], x - X[2]]
M = [X[0] - X[1], X[0] - X[2], X[1] - X[2]]
P = prod(N)
Q = prod(M)

def f(i):

    P = P/N[i]
    Q = Q/M[L - i - 1]
    L = (-1**(i))*P/Q
    return L'''

def f(val, i):
    result = val**3 - (SUM - X[i])*(val**2) + (sumpro[i])*val - PROD/X[i]
    return result

def df(val, i):
    result = 3*val**2 - 2*val*(SUM - X[i]) + (sumpro[i])
    return result

const = [0]*n
L = [0]*n
dL = L.copy()
H = [0]*n
Hcap = H.copy()
FINAL = 0


for i in range(n):

    const[i] = f(X[i], i)
    L[i] = f(x, i)/const[i]
    dL[i] = df(X[i], i)/const[i]

    H[i] = (1 - 2*(x - X[i])*dL[i])*(L[i]**2)
    Hcap[i] = (x - X[i])*(L[i]**2)

    FINAL += H[i]*F[i] + Hcap[i]*DF[i]

    print(i, "L:", L[i])
    print("  dL:", dL[i])
    print("  H:", H[i])
    print("  Hcap:", Hcap[i])
    print("\n")

print("H(", x, ") = ", FINAL)
