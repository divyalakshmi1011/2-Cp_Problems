# Recursion-Only powersOf3ToN(n) [15 pts]
# Write the function powersOf3ToN(n) that takes a possibly-negative float or int n, and returns a list of the 
# positive powers of 3 up to and including n. As an example, powersOf3ToN(10.5) returns [1, 3, 9]. If no such powers 
# of 3 exist, you should return the empty list. You may not use loops/iteration in this problem. 

l = []
i = 0
def recursion_powersof3ton(n):
	# Your code goes here
	if(n < 0 or n == 0):
		return None
	global i
	x = 3 ** i
	if(x <= n):
		i = i + 1
		l.append(x)
		return recursion_powersof3ton(n)
	else:
		if(len(l) == 0):
			return None
		return l

print(recursion_powersof3ton(0.99))
