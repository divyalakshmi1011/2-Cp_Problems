# nthLychrelNumber(n) [20 pts]
# A Lychrel number is a natural number that cannot form a palindrome through the iterative process of 
# repeatedly reversing its digits and adding the resulting numbers. This process is sometimes called the 
# 196-algorithm, after the most famous number associated with the process.
# The first few Lychrel numbers are 196, 295, 394, 493, 592, 689, 691, 788, 790, 879, 887….

def isPalindrome(number):
	return number == reverse(number);  

def reverse(number):
	reverse = 0
	while (number > 0):
		remainder = number % 10
		reverse = (reverse * 10) + remainder
		number = int(number / 10)
	return reverse

def islychrel(n):
	iter = 25
	for i in range(iter):
		n = n + reverse(n)
		if(isPalindrome(n)):
			return False
	return True

def nthlychrelnumbers(n):
	count = 0
	l = 196
	while(count <= n):
		if(islychrel(l)):
			count = count + 1
			if(count == n):
				break
			else:
				l += 1
		else:
			l += 1
	return l


print(nthlychrelnumbers(5))