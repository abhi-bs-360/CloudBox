from math import *
import numpy as np

#Partial derivative value vectors

P = lambda x,y: [2*x, 2*y]
Q = lambda x,y: [y, x]
#R = lambda x,y: [0, 0, 12+cos(z)]

#Evaluates the value of Jacobian vector and functions given

Jacobi = lambda x, y: [P(x,y), Q(x,y)]
Function = lambda x, y: [[x**2 + y**2 - 1.12], [x*y - 0.23]]

#Initialisation

x0 = 0.8
y0 = 0.23
#z0 = 1/12
error = 10**(-4)

condition = True
itr = 0
while condition:

    #Inverse calculation
    Jinv = np.linalg.inv(Jacobi(x0, y0))

    print(Jinv)
    print('\n')

    F = Function(x0, y0)

    #Dot product of inverse_Jacobi and Function vector
    matrix = np.dot(Jinv, F)

    x1 = x0 - matrix[0][0]
    y1 = y0 - matrix[1][0]
    #z1 = z0 - matrix[2][0]

    itr += 1
    print(itr, "-Solution Vector : ", [x1, y1])
    print('\n')

    if (abs(x1 - x0) < error) and (abs(y1 - y0) < error):
        condition = False

    else:
        condition = True
        x0 = x1
        y0 = y1
