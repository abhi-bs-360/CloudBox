from math import *
from cmath import *

def f(x):

	y = 600*x**4 - 550*x**3 + 200*x**2 - 20*x - 1
	return y

p0, p1, p2 = [0.1, 0.5, 1]
tolerance = 10**(-4)

h1, h2 = [p1 - p0, p2 - p1]

delta1 = (f(p1) - f(p0))/h1
delta2 = (f(p2) - f(p1))/h2
d = (delta2 - delta1)/(h1 + h2)

i = 0

while True:

	b = delta2 + h2*d
	D = sqrt(b*b - 4*d*f(p2))

	'''if abs(b - D) < abs(b + D):
		E = b + D
	else:
		E = b - D'''

	signB = abs(b)/b
	E = b + D*signB

	H = -2*f(p2)/E
	P = p2 + H
	i += 1

	print(i, " :", P)
	print("\n")

	if abs(H) < tolerance:
		break

	p0 = p1
	p1 = p2
	p2 = P

	h1 = p1 - p0
	h2 = p2 - p1
	delta1 = (f(p1) - f(p0))/h1
	delta2 = (f(p2) - f(p1))/h2

	d = (delta2 - delta1)/(h1 + h2)
