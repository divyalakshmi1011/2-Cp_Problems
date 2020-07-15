# Write the function pascalsTriangleValue(row, col) 
# that takes int values row and col, and returns the 
# value in the given row and column of Pascal's 
# Triangle where the triangle starts at row 0, and 
# each row starts at column 0. If either row or col 
# are not legal values, return None, instead of crashing. 


# def combination(n, k):
#     if k == 0 or k == n:
#         return str(1)
#     else:
#         return combination(str(n-1, k-1)) + combination(str(n-1,k))

import sys
sys.setrecursionlimit(10**4) 
print(sys.getrecursionlimit())

def fun_pascaltrianglevalue(row, col):
	if col == row or col == 0 or row == 0:
		return 1
	else:
		return fun_pascaltrianglevalue(row - 1, col - 1) + fun_pascaltrianglevalue(row - 1, col)

print(fun_pascaltrianglevalue(3,5))
# print(sys.getrecursionlimit())
