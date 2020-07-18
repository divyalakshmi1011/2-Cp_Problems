# isRotation(x, y) [15 pts]
# Write the function isRotation(x, y) that takes two non-negative integers x and y, both 
# guaranteed to not contain any 0's, and 
# returns True if x is a rotation of the digits of y and False otherwise. For example, 
# 3412 is a rotation of 1234. Any number 
# is a rotation of itself.
def fun_rotatestrings(s, n):
	l = len(s)
	for i in range(n):
		s = s[1:] + s[:1]
	return s
	

def isrotation(x, y):
	# Your code goes here
	if(x == y):
		return True
	t = str(x)
	if(t[::-1] == str(y)):
		return True
	for i in range(len(t)):
		r = fun_rotatestrings(t,i)
		if(int(r) == y):
			return True
	return False

print(isrotation(3142, 1234))