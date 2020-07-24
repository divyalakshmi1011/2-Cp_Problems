# nthAutomorphicNumbers(n) [20 pts]
# In mathematics, an automorphic number is a number whose square "ends" in the same digits as the 
# number itself. For example, 5^2 = 25, 6^2 = 36, 76^2 = 5776, and 890625^2 = 793212890625, so 5, 6, 
# 76 and 890625 are all automorphic numbers.

def nthautomorphicnumbers(n):
	# Your code goes here
	if(n == 1):
		return 0
	count = 1
	a = 1
	while(count <= n):
		sqr = a ** 2
		s1 = str(a)
		s2 = str(sqr)
		l = len(s1)
		x = s2[-l:]
		if(a == int(x)):
			count = count + 1
			if(count == n):
				break
			else : a += 1
		else:
			a += 1
	return a

print(nthautomorphicnumbers(0))
print(nthautomorphicnumbers(1))
print(nthautomorphicnumbers(2))
print(nthautomorphicnumbers(3))
print(nthautomorphicnumbers(4))
print(nthautomorphicnumbers(5))
print(nthautomorphicnumbers(6))
print(nthautomorphicnumbers(7))
print(nthautomorphicnumbers(8))