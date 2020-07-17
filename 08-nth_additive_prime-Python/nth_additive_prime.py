# Write the function fun_nth_additive_prime(n) that takes a non-negative int n 
# and returns the nth Additive Prime, which is a prime number such that 
# the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5 
# is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2


def isprime(n):
	i = 1
	count = 0
	while(i <= n):
		if(n%i == 0):
			count = count + 1
		i = i + 1
	if(count == 2):
		return True
	else:
		return False

def isadditive(n):
	s = str(n)
	for i in s:
		t = int(i)
		x = isprime(t)
		print(x,t)
		if(x == False):
			return False
	return True

def fun_nth_additive_prime(n):
	if(isprime(n) and isadditive(n)):
		return True
	else:
		return False

print(fun_nth_additive_prime(113))