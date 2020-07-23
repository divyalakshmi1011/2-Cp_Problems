# Background: a Kaprekar number is a non-negative integer, the representation of whose square 
# can be split into two possibly-different-length parts (where the right part is not zero) 
# that add up to the original number again. For instance, 45 is a Kaprekar number, because 
# 45**2 = 2025 and 20+25 = 45. You can read more about Kaprekar numbers here. The first several 
# Kaprekar numbers are: 1, 9, 45, 55, 99, 297, 703, 999 , 2223, 2728,... 
# With this in mind, write the function nthKaprekarNumber(n) that takes a non-negative int n 
# and returns the nth Kaprekar number, where as usual we start counting at n==0.


import math

def fun_nth_kaprekarnumber(n):
    if(n == 0):
        return 1
    count = 0
    k = 2
    while(count <= n):
        b = (k ** 2) % (10 ** 2)
        a = (k ** 2 - b)//(10 ** 2)
        if((a + b) == k):
            count = count + 1
            if(count == n):
                break
            else:
                k = k + 1
        else:
            k = k + 1
    return k

print(fun_nth_kaprekarnumber(1))