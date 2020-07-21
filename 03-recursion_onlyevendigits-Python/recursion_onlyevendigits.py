# Without using iteration and without using strings, 
# write the recursive function onlyEvenDigits(L), 
# that takes a list L of non-negative integers 
# (you may assume that), and returns a new list of 
# the same numbers only without their odd digits 
# (if that leaves no digits, then replace the number with 0). 
# So: onlyEvenDigits([43, 23265, 17, 58344]) returns [4, 226, 0, 844]. 
# Also the function returns the empty list if the original list is empty. 
# Remember to not use strings. You may not use loops/iteration in this problem.

def evenlis(lis):  
    if len(lis) == 0:
        return []  
    else:
        return [lis[0]] if lis[0] % 2 == 0 else [] + evenlis(lis[1:])

print(evenlis([143]))
def fun_recursion_onlyevendigits(l): 
		return []