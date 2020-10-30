from math import *

def u_cal(u, n):

    temp = u;
    for i in range(1, n):
        temp = temp * (u - i);
    return temp

def fact(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

'''def binCoeff(u, i):
    f = comb(u, i)
    return f'''

# Driver Code
n = 4
x = [ 45, 50, 55, 60 ]


y = [[0 for i in range(n)] for j in range(n)]
y[0][0] = 0.7071
y[1][0] = 0.7660
y[2][0] = 0.8192
y[3][0] = 0.8660

# Calculating the forward difference table
for i in range(1, n):
    for j in range(n - i):
        y[j][i] = y[j + 1][i - 1] - y[j][i - 1]

# Displaying the forward difference table
print("X\tY\ty1\ty2\y3\n")
for i in range(n):
    print(x[i], end = "\t")
    for j in range(n - i):
        print(y[i][j], end = "\t")
    print("")

# Value to interpolate at
value = 52

# initializing u and sum
sum = y[0][0]
u = (value - x[0]) / (x[1] - x[0])
for i in range(1,n):
    sum = sum + (u_cal(u, i) * y[0][i]) / fact(i)

print("\nValue at", value, "is", round(sum, 6))
