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
		return False
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
    if(n == 0):
        return 2
    p = 3
    count = 0
    while(count <= n):
        s = str(p)
        if(len(s) == 1):
            if(isprime(p)):
                count = count + 1
                print("1",count,p)
                if(count == n):
                    break
                else:
                    p = p + 1
            else:
                p = p + 1
        elif(len(s) == 2):
            print("p",p)
            if(isprime(p)):
                if(isprime(int(s[1]))):
                    count = count + 1
                    print("2",count,p,n)
                    if(count == n):
                        print("divya",count,p,n)
                        break
                    else:
                        p = p + 1
                else:
                    p = p + 1
            else:
                p = p + 1
        else:
            flag = True
            if(isprime(p) and '0' not in s):
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
            else:
                p = p + 1
    return p

print(fun_nth_lefttruncatableprime(25))
