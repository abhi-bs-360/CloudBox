f1 = lambda x1,x2,x3,x4: (6 - 2*x3 + x2)/10
f2 = lambda x1,x2,x3,x4: (x1 + x3 - 3*x4 + 25)/11
f3 = lambda x1,x2,x3,x4: (-2*x1 + x2 + x4 -11)/10
f4 = lambda x1,x2,x3,x4: (-3*x2 + x3 + 15)/8
# Initial setup

x10 = 0
x20 = 0
x30 = 0
x40 = 0
count = 1

# Reading tolerable error
e = 0.0001

condition = True

while condition:
    x1 = f1(x10,x20,x30, x40)
    x2 = f2(x10,x20,x30, x40)
    x3 = f3(x10,x20,x30, x40)
    x4 = f4(x10,x20,x30, x40)

    print(count, "Solution set : ", [x1, x2, x3, x4])
    print("\n")
    e1 = abs(x10-x1)
    e2 = abs(x20-x2)
    e3 = abs(x30-x3)
    e4 = abs(x40-x4)

    count += 1
    x10 = x1
    x20 = x2
    x30 = x3
    x40 = x4

    condition = e1 > e or e2 > e or e3 > e or e4 > e
