from math import *


[b, c, e] = [5, 7, 6]
tita2 = radians(30)
w2 = 50

try:
    tita3 = asin((e - b*sin(tita2))/c)
    a = b*cos(tita2) +  c*cos(tita3)

    w3 = -b*w2*cos(tita2)/(c*cos(tita3))
    vBlock = -b*w2*sin(tita2) + w3*c*sin(tita3)

except:
    print("Errr")

print("@3 : ", degrees(tita3))
print("A(x) : ", a)
print("W3 : ", w3)
print("Velocity of Block :", vBlock)
