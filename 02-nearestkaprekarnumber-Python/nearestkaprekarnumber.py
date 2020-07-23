# Note: please do not start this problem prior to completing previous problem. 
# Bearing in mind the definition of Kaprekar Number from above problem, write the function 
# nearestKaprekarNumber(n) that takes an int value n and returns the Kaprekar number 
# closest to n, with ties going to smaller value. For example, nearestKaprekarNumber(49) returns 45, 
# and nearestKaprekarNumber(51) returns 55. And since ties go to the smaller number, 
# nearestKaprekarNumber(50) returns 45. 
# Note: as you probably guessed, this also cannot be solved by counting up from 0, 
# as that will not be efficient enough to get past the autograder. 
# Hint: one way to solve this is to start at n and grow in each direction until you find a Kaprekar number.



import math
def iskapre(n):
    sqr = n ** 2
    digits = str(sqr)
    l = len(digits)
    for i in range(1,l):
        left = int("".join(digits[:i]))
        right = int("".join(digits[i:]))
        if(left + right == n and left != 0 and right != 0):
            return True
    return False

print(iskapre(45))
def fun_nearestkaprekarnumber(n):
    return 1