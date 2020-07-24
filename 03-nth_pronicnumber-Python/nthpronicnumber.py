# nthPronicNumber(n) [20 pts]
# Write the function nthPronicNumber that takes a non-negative int n and returns the nth Pronic 
# Number. Pronic number is a number which is the product of two consecutive integers, that is, a 
# number n is a product of x and (x+1).
def factors(n):
    l = []
    for i in range(2,n + 1):
        if(n % i == 0):
                l.append(i)
    return l
def ispronic(n):
	l = factors(n)
	for i in range(len(l) - 1):
		# print(l[i],l[i + 1])
		if(l[i] == l[i + 1] - 1 and (l[i] * l[i + 1] == n)):
			print(l[i],l[i + 1])
			return True
	return False

def nthpronicnumber(n):
	# Your code goes here
	if(n == 0):
		return 0
	if(n == 1):
		return 2
	c = 2
	count = 1
	while(count <= n):
		# print("c",c)
		if(ispronic(c)):
			print("divya",c)
			count += 1
			if(count == n):
				break
			else: c += 1
		else: c += 1
	return c

print(nthpronicnumber(5))