# nthPronicNumber(n) [20 pts]
# Write the function nthPronicNumber that takes a non-negative int n and returns the nth Pronic 
# Number. Pronic number is a number which is the product of two consecutive integers, that is, a 
# number n is a product of x and (x+1).
def factors(n):
    l = []
    for i in range(1,n + 1):
        if(n % i == 0):
                l.append(i)
    return l

def nthpronicnumber(n):
	# Your code goes here
	pass