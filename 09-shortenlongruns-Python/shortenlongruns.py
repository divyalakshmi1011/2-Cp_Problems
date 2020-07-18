# shortenLongRuns(L, k) [15 pts]
# Write the non-destructive function shortenLongRuns(L, k) that takes a list L and a positive integer k, and 
# non-destructively returns a similar list, only without any run of k consecutive equal values in L. This means that 
# any values that would otherwise produce a consecutive run of k elements are not present. 
# For example: 
# assert(shortenLongRuns([2, 3, 5, 5, 5, 3], 2) == [2, 3, 5, 3]) 
# assert(shortenLongRuns([2, 3, 5, 5, 5, 3], 3) == [2, 3, 5, 5, 3]) 
# Note: your function may not just create a copy of L and call the destructive version of this function (below) on 
# that copy and return it. Instead, you must directly construct the result here.

def lookandsay(a):
    print(type(a))
    b = a
    b.append(" ")
    print(b)
    result = []
    repeat = b[0]
    b = b[1:]
    count = 1
    if(len(a) == 0):
        return result
    for item in b:
        if item != repeat:
            result.append((count,int(repeat)))
            count = 1
            repeat = item
        else:
            count += 1
    return result

def shortenlongruns(L, k):
	m = lookandsay(L)
	# Your code goes here
	l = []
	if(len(L) == 0):
		return l
	for item in m:
		if(len(item) == 0):
			return l
		for i in range(item[0]):
			if(i == k - 1):
				break
			l.append(item[1])
	return l

print(shortenlongruns([2, 3, 5, 5, 5, 3], 3))