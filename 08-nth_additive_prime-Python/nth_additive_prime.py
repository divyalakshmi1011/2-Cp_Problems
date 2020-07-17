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
	if(count == 2):
		return True
	else:
		False

def fun_nth_additive_prime(n):
	return 1