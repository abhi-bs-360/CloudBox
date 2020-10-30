from math import *

'''def f(x):
    y =
    return y'''

X = [1, 1.3, 1.6, 1.9, 2.2]
#FX = [f(X[0]), f(X[1]), f(X[2]), f(X[3]), f(X[4]), f(X[5])]
FX = [0.7651977, 0.6200860, 0.4554022, 0.2818186, 0.1103623]

print("f(", X, ") =", FX)
print('\n\n')
m = -1

while m < 3:

    box = FX
    FX = list()
    m += 1

    for i in range(len(box) - 1):
        val = (box[i + 1] - box[i])/(X[i + 1 + m] - X[i])
        FX.append(val)

    print((m+1),".f = ", FX)
    print('\n')
