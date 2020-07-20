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
    for i in range(0, len(arr)): 
        sum = 0
        for j in range(0, len(arr[0])): 
            if (i == j): 
                d1 += arr[i][j] 
            if (i == len(arr[0]) - j - 1): 
                d2 += arr[i][j]
            sum += arr[i][j]
        l.append(sum)
    l.append(d1)
    l.append(d2)
    return l


def fixmostlymagicsquare(L):
	k = ismostlymagicsquare(L)
	if len(set(k)) == 1 :
		return L
	else:
		x = list(set(k))
		return x[1]

print(fixmostlymagicsquare([[2, 7, 9], [9, 5, 1], [4, 3, 8]]))