# Write the function fun_distance(x1, y1, x2, y2) 
# that takes four int values x1, y1, x2, y2 
# that represent the two points (x1, y1) and (x2, y2), 
# and returns the distance between those points as a int.
import math
from math import sqrt

def fun_distance(x1, y1, x2, y2):
	a = (x2-x1)**2
	b = (y2-y1)**2
	d = sqrt(a + b)
	# your code goes here
	return d