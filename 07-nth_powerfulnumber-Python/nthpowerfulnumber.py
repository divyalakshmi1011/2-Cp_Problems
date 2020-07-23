# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.

def prime(n): 
	return all([(n % j) for j in range(2, int(n**0.5)+1)]) and n>1

def factors(n):
	L=[]
	for i in range(1,n):
		if(n % i == 0):
			if(prime(i)):
				L.append(i)
	return L

def nthpowerfulnumber(n):
	# Your code goes here
	if(n == 0):
		return 1
	count = 0
	p = 2
	while(count <= n):
		l = factors(p)
		flag = True
		for i in l:
			if(p % (i**2) != 0):
				flag = False
		if(flag):
			count = count + 1
		if(count == n):
			break
		else:
			p = p + 1
	return p

print(nthpowerfulnumber(1))
