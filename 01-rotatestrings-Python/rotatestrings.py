# Write the function rotatestring(s, k) that takes a string s and a possibly-negative integer k. 
# If k is non-negative, the function returns the string s rotated k places to the left. 
# If k is negative, the function returns the string s rotated |k| places to the right. So, for example:
# assert(rotateString('abcd',  1) == 'bcda')
# assert(rotateString('abcd', -1) == 'dabc')



def fun_rotatestrings(s, n):
	l = len(s)
	if(n > 0):
		for i in range(n):
			s = s[1:] + s[:1]
		return s
	elif n < 0:
		for i in range(-(n)):
			s = s[l - 1] + s[: (l-1)]
		return s
	else:
		return s

print(fun_rotatestrings("abcd",-6))
print(fun_rotatestrings("ac323",0))

