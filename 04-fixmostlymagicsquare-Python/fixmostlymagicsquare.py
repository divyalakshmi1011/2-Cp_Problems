# fixMostlyMagicSquare(L) [15 pts]
# In this week's writing session, we wrote isMostlyMagicSquare(L). Here, say we have a mostly magic square L, but 
# then we modify L by changing exactly one value in L so that it no longer is a mostly magic square. For this 
# exercise, we assume we have just such a list L, and your task is to find and fix that change. So, given the list 
# L, return a new list M such that M is the same as L, only with exactly one value changed, and M is a mostly magic 
# square.
def ismostlymagicsquare(arr):
    d1 = 0
    d2 = 0
    l = []
    for col in range(len(arr)):
        l.append(sum(row[col] for row in arr))
    for i in range(0, len(arr)): 
        s = 0
        for j in range(0, len(arr[0])): 
            if (i == j): 
                d1 += arr[i][j] 
            if (i == len(arr[0]) - j - 1): 
                d2 += arr[i][j]
            s += arr[i][j]
        l.append(s)
    l.append(d1)
    l.append(d2)
    return l

def most_frequent(List): 
    return max(set(List), key = List.count) 

def fixmostlymagicsquare(L):
	k = ismostlymagicsquare(L)
	if len(set(k)) == 1 :
		return L
	else:
		x = most_frequent(k)
		for itrm in set(k):
			if itrm != x:
				y = itrm
		diff = x - y
		for i in range(len(L)):
			for j in range(len(L[0])):
				a = L[i][j]
				L[i][j] = L[i][j] + diff
				v = ismostlymagicsquare(L)
				print(v)
				if(len(set(v)) == 1):
					print(L)
					b = L
					break
				else:
					L[i][j] = a
		return b



print(fixmostlymagicsquare([[16, 3, 2, 13], [5, 10, 11, 18], [9, 6, 7, 12],[4, 15, 14, 1]]))