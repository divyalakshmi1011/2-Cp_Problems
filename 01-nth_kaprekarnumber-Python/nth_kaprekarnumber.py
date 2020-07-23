# Background: a Kaprekar number is a non-negative integer, the representation of whose square 
# can be split into two possibly-different-length parts (where the right part is not zero) 
# that add up to the original number again. For instance, 45 is a Kaprekar number, because 
# 45**2 = 2025 and 20+25 = 45. You can read more about Kaprekar numbers here. The first several 
# Kaprekar numbers are: 1, 9, 45, 55, 99, 297, 703, 999 , 2223, 2728,... 
# With this in mind, write the function nthKaprekarNumber(n) that takes a non-negative int n 
# and returns the nth Kaprekar number, where as usual we start counting at n==0.


import math

def fun_nth_kaprekarnumber(n):
    count = 0
    k = 1
    while(count <= n):
        # print(k, "count",count)
        sqr = k ** 2
        digits = str(sqr)
        l = len(digits)
        for i in range(1,l):
            # print("l",l)
            left = int("".join(digits[:i]))
            right = int("".join(digits[i:]))
            # print(left,right,sqr)
            if(left + right == k and left != 0 and right != 0):
                # print("divya")
                count = count + 1
                break
        if(count == n):
            break
        else:
            k = k + 1
    return k

print(fun_nth_kaprekarnumber(0))
print(fun_nth_kaprekarnumber(1))
print(fun_nth_kaprekarnumber(2))
print(fun_nth_kaprekarnumber(3))
print(fun_nth_kaprekarnumber(4))
print(fun_nth_kaprekarnumber(5))
print(fun_nth_kaprekarnumber(6))
print(fun_nth_kaprekarnumber(7))
print(fun_nth_kaprekarnumber(8))
print(fun_nth_kaprekarnumber(9))
print(fun_nth_kaprekarnumber(10))