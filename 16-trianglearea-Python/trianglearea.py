# trianglearea(s1, s2, s3)[5pts]
# Write the function trianglearea(s1, s2, s3) that takes 3 floats/ints and returns the area of the
# triangle that has those lengths of its side. If no such triangle exists, return 0. Hint: you
# will probably wish to use Heron's Formula.
import math

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
