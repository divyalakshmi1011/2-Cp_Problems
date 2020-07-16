# median(a) (10 pts)
# Write the non-destructive function median(a) that takes a list of ints or floats and returns the median value, 
# which is the value of the middle element, or the average of the two middle elements if there is no single middle 
# element. If the list is empty, return None.

def median(a):
	n_num = list(a)
	n = len(n_num)
	if(n == 0):
		return None
	n_num.sort() 
	if n % 2 == 0: 
		median1 = n_num[n//2] 
		median2 = n_num[n//2 - 1] 
		median = (median1 + median2)/2
	else: 
		median = n_num[n//2]
	return median