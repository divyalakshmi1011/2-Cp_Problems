# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 



def fun_set_kth_digit(n, k, d):
	s = str(n)
	if(k < len(s)):
		c = s[::-1]
		c[k] = d
		return int(c[::-1])
	elif(k == len(s)):
		c = s[::-1]
		c += str(d)
		return int(c[::-1])
	else:
		return 0

