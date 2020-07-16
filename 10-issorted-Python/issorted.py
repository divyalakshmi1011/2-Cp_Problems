# isSorted(a) (10 Pts)
# Write the function isSorted(a) that takes a list of numbers and returns True if the list 
# is sorted (either smallest-first or largest-first) and False otherwise. Your function 
# must only consider each value in the list once (so, in terms of big-oh, which we will 
# learn soon, it runs in O(n) time, where n=len(a)), and so in particular you may not sort 
# the list.

def issorted(a):
	s = False
	for i in range(len(a) - 2):
		if(a[i] <= a[i + 1]):
			if(a[i + 1] > a[i + 2]):
				s = True
		elif(a[i] > a[i + 1]):
			if(a[i + 1] < a[i + 2]):
				s = True
	if(s):
		return False
	else:
		return True

print(issorted([5,4,3,2,1]))