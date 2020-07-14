# Write the function circlesIntersect(x1, y1, r1, x2, y2, r2) 
# that takes 6 numbers (ints) -- x1, y1, r1, x2, y2, r2 -- 
# that describe the circle centered at (x1,y1) with radius r1, 
# and the circle centered at (x2,y2) with radius r2, and returns True 
# if the two circles intersect and False otherwise.
import math
from math import sqrt

def fun_circlesintersect(x1, y1, r1, x2, y2, r2):
	d = fun_distance(x1,y1,x2,y2)
	if((r1 - r2) < d < (r1 + r2)):
		return True
	# your code goes here
	return False 

def fun_distance(x1, y1, x2, y2):
	a = (x2-x1)**2
	b = (y2-y1)**2
	d = sqrt(a + b)
	# your code goes here
	return int(d)
