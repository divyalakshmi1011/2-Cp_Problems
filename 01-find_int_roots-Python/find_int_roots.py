# Write the function bonusFindIntRoots(a,b,c) that takes 
# the int coefficients a, b, c of a quadratic equation of this form:
#      y = ax2 + bx + c
# You are guaranteed the function has 2 real roots, and in fact that 
# the roots are all integers. Your function should return these 2 int roots 
# in increasing order. How does a function return multiple values? Like so:
# return root1, root2

import math
from math import sqrt
def fun_find_int_roots(a, b, c):
	r = b**2  - 4*a*c
	r1 = (((-b) - sqrt(r)) / (2*a))
	r2 = (((-b) + sqrt(r)) / (2*a))
	return r1, r2


