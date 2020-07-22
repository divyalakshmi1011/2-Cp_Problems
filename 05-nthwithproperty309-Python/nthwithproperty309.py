# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.

def nthwithproperty309(n):
	# Your code goes here
	if(n == 0):
		return 309
	x = n**5
	s = str(x)
	i = 310
	count = 0
	while(count <= n):
		print(i)
		x = i**5
		s = str(x)
		if('0' in s and '1' in s and '2' in s and '3' in s and '4' in s and '5' in s and '6' in s and '7' in s and '8' in s and '9' in s):
			count = count + 1
			if(count == n):
				break
			else:
				i = i + 1
		else:
			i = i + 1
	return i

print(nthwithproperty309(3))