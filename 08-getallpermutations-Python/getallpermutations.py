# getallPermutations(str) [20 pts]
# Write an efficient program to print all permutations of a given String. For example, if given input is "abc" then 
# your program should print all 6 permutations e.g. [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]
from itertools import permutations

def permute(l,s,e,p):
	if s == e:
		p.append(tuple(l))
	else:
		for i in range(s,e+1):
			l[s], l[i] = l[i], l[s]
			permute(l, s+1, e,p)
			l[s], l[i] = l[i], l[s]
def getallpermutations(x):
	s = 0
	e = len(x) - 1
	l = list(x)
	p = []
	permute(l,s,e,p)
	p.sort()
	return p

print(getallpermutations("xyza"))
print(list(permutations("xyza", r=len("xyza"))))