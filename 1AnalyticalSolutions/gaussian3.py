f1 = lambda x1,x2,x3: (7+x1)/2
f2 = lambda x1,x2,x3: (1+x3+x1)/2
f3 = lambda x1,x2,x3: (1+1.5*x2)/2
# Initial setup

x10 = 1
x20 = 1
x30 = 1
count = 1

# Reading tolerable error
e = 0.00001

condition = True

while condition:
    x1 = f1(x10,x20,x30)
    x2 = f2(x1,x20,x30)
    x3 = f3(x1,x2,x30)

    print(count, "Solution Set : ", [x1, x2, x3])
    print('\n')
    e1 = abs(x10-x1)
    e2 = abs(x20-x2)
    e3 = abs(x30-x3)

    count += 1
    x10 = x1
    x20 = x2
    x30 = x3

    condition = (e1 > e) or (e2 > e) or (e3 > e)
