# Write the function nthLeftTruncatablePrime(n).
# A Left-truncatable prime is a prime which in a given base (say 10) does not contain 0 
# and which remains prime when the leading (left) digit is successively removed. 
# For example, 317 is left-truncatable prime since 317, 17 and 7 are all prime. 
# There are total 4260 left-truncatable primes.
# So nthLeftTruncatablePrime(0) retunearestKaprekarNumber(n)rns 2, and 
# nthLeftTruncatablePrime(10) returns 53.



import math

def isprime(n):
	if(n == 1):
		return True
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

def fun_nth_lefttruncatableprime(n):
    p = 2
    count = 0
    while(count <= n):
        s = str(p)
        if(len(s) == 1):
            if(isprime(p)):
                print(count,p)
                count = count + 1
                if(count == n):
                    break
                else:
                    p = p + 1
            else:
                p = p + 1
        else:
            flag = True
            for i in range(len(s) - 1):
                if(not isprime(int(s[i + 1:]))):
                    flag = False
            if(flag):
                print(s)
                count = count + 1
                if(count == n):
                    break
                else:
                    p = p + 1
            else:
                p = p + 1
    return p

print(fun_nth_lefttruncatableprime(5))
