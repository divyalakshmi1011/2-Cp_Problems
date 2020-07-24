# nthCircularPrime(n) [20 pts]
# Write the function nthCircularPrime that takes a non-negative int n and returns the nth 
# Circular prime, which is a prime number that does not contain any 0's and such that all the 
# numbers resulting from rotating its digits are also prime. The first Circular primes are 2, 3, 
# 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197... To see why 197 is a Circular prime, 
# note that 197 is prime, as is 971 (rotated left), as is 719 (rotated left again).
def rotate(input,d):
    Lfirst = input[0 : d] 
    Lsecond = input[d :] 
    Rfirst = input[0 : len(input)-d] 
    Rsecond = input[len(input)-d : ] 
    return (Lsecond + Lfirst)

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
def repetency(str):
    for i in range(len(str)):
        for j in range(i + 1,len(str)):
            if(str[i] != str[j]):
                return True
    return False

def nthcircularprime(n):
	p = 2
	count = 0
	while(count <= n):
		s = str(p)
		if(len(s) == 1):
			if(isprime(p)):
				count = count + 1
				if(count == n):break
				else: p = p + 1
			else:
				p = p + 1
		else:
			flag = True
			if(repetency(s)):
				for i in range(len(s)):
					d = rotate(s,i)
					# print("before",d,i)
					if(not isprime(int(d))):
						# print(d,i)
						flag = False
				if(flag):
					count = count + 1
				if(count == n):
					break
				else:
					p = p + 1
			else: p = p + 1
	return p

print(nthcircularprime(10))
print(nthcircularprime(11))
print(nthcircularprime(12))
print(nthcircularprime(13))
