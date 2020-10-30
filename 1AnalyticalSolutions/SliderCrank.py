from math import *

[l1, l2, l3] = [0, 0.12, 0.26]
tita2 = radians(65)
w2 = 1.6

tita3 = asin((l1 + l2*sin(tita2))/l3)
gamma = degrees(pi - tita2 - tita3)
print("Gamma : ", [gamma, 180 - gamma, gamma - 90])


X = l2*cos(tita2) + l3*cos(tita3)
w3 = -l2*w2*cos(tita2)/(l3*cos(tita3))
vBlock = -l2*w2*sin(tita2) + w3*l3*sin(tita3)

tita3 = degrees(tita3)
print(f"@3 : {tita3}  \tDist(x) : {X}\nw3 : {w3} \tvBlock : {vBlock}")
