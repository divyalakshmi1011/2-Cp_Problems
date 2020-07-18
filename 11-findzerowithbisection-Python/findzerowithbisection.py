# Bisection Algorithm comes into play!
# We know that the square root of x lies between 1 and x, from mathematics
# Rather than exhaustively trying things starting at 1, suppose instead we pick a number in the middle of this range
# Bisection search works when value of function varies monotonically with input
# If g, the users input/guess, is less than/greater than the midpoint of the range, then that number becomes the new high point of said range and is then factored into the new search.

def findzerowithbisection(x, epsilon):
	# epsilon and step are initialized
	# don't change these values
	# epsilon
	# your code starts here
	low = 0.0
	high = x
	middle = float((low + high)/2)
	while(abs((middle)**2 - x) >= epsilon):
		# print(abs((middle)**2))
		if(((middle)**2) > x):
			# print(middle,x,1)
			high = middle
		elif(((middle)**2) < x):
			# print(middle,x,2)
			low = middle
		else:
			# print(middle,x)
			break
		middle = (low + high)/2
	return middle

print(findzerowithbisection(25, 0.01))