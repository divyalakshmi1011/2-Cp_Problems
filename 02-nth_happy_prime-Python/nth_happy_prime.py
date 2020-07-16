# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).

def prime(n): 
	return all([(n % j) for j in range(2, int(n**0.5)+1)]) and n>1


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

def fun_nth_happy_prime(n):
	if(n == 0):
		return 1
	if(n == 1):
		return 7
	i = 2
	count = 1
	while(count <= n):
		print(i)
		if(ishappynumber(i) and prime(i)):
			print("bnm",i)
			count = count + 1
			if(count == n):
				return i
		i = i + 1