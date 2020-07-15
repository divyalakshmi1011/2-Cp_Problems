# Write the function nearestOdd(n) that takes an float n, 
# and returns as an int value the nearest odd number to n. 
# In the case of a tie, return the smaller odd value. 
# Note that the result must be an int, so nearestOdd(13.0) is the int 13, and not the float 13.0.



def fun_nearestodd(n):
	s = str(n)
	x = s.split(".")
	a = int(x[0])
	b = int(x[1])
	if(b != 0):
		if(a%2 != 0):
			return a
		else:
			return a + 1
	else:
		if(a%2 != 0):
			return a
		else:
			return a - 1

print(fun_nearestodd(13.7))


