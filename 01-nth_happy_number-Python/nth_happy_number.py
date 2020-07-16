# Write the function nthHappyNumber(n) which takes a non-negative integer 
# and returns the nth happy number (where the 0th happy number is 1). 
# Here are some test assertions for you:
# assert(nthHappyNumber(0) == 1)
# assert(nthHappyNumber(1) == 7)
# assert(nthHappyNumber(2) == 10)
# assert(nthHappyNumber(3) == 13)
# assert(nthHappyNumber(4) == 19)
# assert(nthHappyNumber(5) == 23)
# assert(nthHappyNumber(6) == 28)
# assert(nthHappyNumber(7) == 31)
def ishappynumber(n):
	# your code goes here
	s = str(n)
	if(n == 1):
		return True
	if(len(s) == 1 or n < 0):
		return False
	else:
		while(len(s) > 1):
			sum = 0
			for item in s:
				sum += ((int(item)) ** 2)
			s = str(sum)
		if(int(s) == 1):
			return True
		else:
			return False

def fun_nth_happy_number(n):
	if(n == 0):
		return 1
	i = 1
	count = 0
	while(i <= n):
		print(i)
		if(ishappynumber(i)):
			count = count + 1
			if(count == n):
				return i
		i = i + 1

print(fun_nth_happy_number(6))
