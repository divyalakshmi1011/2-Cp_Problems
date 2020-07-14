# isrighttriangle(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function isrighttriangle(x1, y1, x2, y2, x3, y3) that takes 6 int or float values that
# represent the vertices (x1,y1), (x2,y2), and (x3,y3) of a triangle, and returns True if that is
# a right triangle and False otherwise. You may wish to write a helper function,
# distance(x1, y1, x2, y2), which you might call several times. Also, remember to use
# almostEqual (instead of ==) when comparing floats.
import math
from math import sqrt

def fun_distance(x1, y1, x2, y2):
	a = (x2-x1)**2
	b = (y2-y1)**2
	d = sqrt(a + b)
	# your code goes here
	return d

def isrighttriangle(x1, y1, x2, y2, x3, y3):
	a = fun_distance(x1,y1,x2,y2)
	b = fun_distance(x2,y2,x3,y3)
	c = fun_distance(x1,y1,x3,y3)
	if math.isclose((a**2) ,(b**2 + c**2)) or math.isclose((b**2), (c**2 + a**2)) or math.isclose((c**2), (a**2 + b**2)):
		return True
	else:
		return False

print(isrighttriangle(13, -1, -9, 3, -3, -9))