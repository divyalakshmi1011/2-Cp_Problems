# Write the function circlesIntersect(x1, y1, r1, x2, y2, r2) 
# that takes 6 numbers (ints) -- x1, y1, r1, x2, y2, r2 -- 
# that describe the circle centered at (x1,y1) with radius r1, 
# and the circle centered at (x2,y2) with radius r2, and returns True 
# if the two circles intersect and False otherwise.
import math
from math import sqrt

def fun_circlesintersect(x1, y1, r1, x2, y2, r2):
	d = fun_distance(x1,y1,x2,y2)
	if((r1 - r2) <= d <= (r1 + r2)):
		return True
	# your code goes here
	return False 

def fun_distance(x1, y1, x2, y2):
	a = (x2-x1)**2
	b = (y2-y1)**2
	d = sqrt(a + b)
	# your code goes here
	return round(d)

print(fun_circlesintersect(2, 3, 12, 15, 28, 10))
print(fun_circlesintersect(3, 4, 5, 14, 18, 8))
print(fun_circlesintersect(-10, 8, 30, 14, -24, 10))
print(fun_circlesintersect(5, 6, 14, 8, 7, 9))
