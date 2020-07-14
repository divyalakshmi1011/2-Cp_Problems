# triangleareabycoordinates(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function triangleareabycoordinates(x1, y1, x2, y2, x3, y3) that takes 6 int or float
# values that represent the three points (x1,y1), (x2,y2), and (x3,y3), and returns as a float the
# area of the triangle formed by those three points. Hint: you should make constructive use of
# the triangleArea function you just wrote above.
import math
from math import sqrt

def fun_distance(x1, y1, x2, y2):
	a = (x2-x1)**2
	b = (y2-y1)**2
	d = sqrt(a + b)
	# your code goes here
	return d

def islegaltriangle(s1, s2, s3):
	if (s1 + s2 <= s3) or (s1 + s3 <= s2) or (s2 + s3 <= s1) :
		return False
	else:
		return True

def trianglearea(s1, s2, s3):
	# your code goes here
	s = (s1 + s2 + s3) / 2
	if(islegaltriangle(s1,s2,s3)):
		temp = (s)*(s - s1)*(s - s2)*(s - s3)
		area = math.sqrt(temp)
		return area
	else:
		return 0
def triangleareabycoordinates(x1, y1, x2, y2, x3, y3):
	a = fun_distance(x1,y1,x2,y2)
	b = fun_distance(x2,y2,x3,y3)
	c = fun_distance(x1,y1,x3,y3)
	if(islegaltriangle(a,b,c)):
		area = trianglearea(a,b,c)
		return area