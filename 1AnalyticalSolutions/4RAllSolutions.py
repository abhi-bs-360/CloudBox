from math import *

r1, r2, r3, r4 = [0.07, 0.03, 0.1, 0.05]
theta1, theta2, theta3, theta4 = [0, radians(135), radians(17), radians(85)]
w1, w2 = [0, 95]
a1, a2 = [0, 0]

D = sqrt(r1*r1 + r2*r2 - 2*r1*r2*cos(theta2 - theta1))
m = r3*r3 + r4*r4 - D*D
n = 2*r3*r4
gamma = acos(m/n)

Y = r4*sin(gamma) - r2*sin(theta2 - theta1)
X = r1 + r3 - r2*cos(theta2 - theta1) - r4*cos(gamma)
theta3 = 2*atan2(Y, X)

Y = -r3*sin(gamma) + r2*sin(theta2 - theta1)
X = r4 - r1 + r2*cos(theta2 - theta1) - r3*cos(gamma)
theta4 = 2*atan2(Y, X)

k = -w2*r2/sin(gamma)
w3 = k*sin(theta4 - theta2 + theta1)/r3
w4 = k*sin(theta3 - theta2 + theta1)/r4

theta2 -= theta1
a3 = (a2*r2*sin(theta2 - theta4) + (w2**2)*r2*cos(theta2 - theta4) - (w4**2)*r4 + (w3**2)*r3*cos(theta4 - theta3))/(r3*sin(theta4 - theta3))
a4 = (a2*r2*sin(theta2 - theta3) + (w2**2)*r2*cos(theta2 - theta3) + (w3**2)*r3 - (w3**2)*r4*cos(theta4 - theta3))/(r4*sin(theta4 - theta3))

print("@3 : ", degrees(theta3), "  ", degrees(2*pi - theta3))
print("@4 : ", degrees(theta4))
print("w3 : ", w3)
print("w4 : ", w4)
print("Alpha3 : ", a3)
print("Alpha4 : ", a4)
