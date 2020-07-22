# Write the function nthSmithNumber that takes a non-negative int n 
# and returns the nth Smith number, where a Smith number is a composite (non-prime) 
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1). 
# Note that if a prime number divides the Smith number multiple times, its digit sum 
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is 
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22

def isfactor(n):
    fact_list = []
    factor = 2
    if(n == 1):
        fact_list.append(1)
    else:
        while True:
            if(n % factor) == 0 :
                fact_list.append(factor)
                n = n // factor
                if(n == 1):
                    break
            else:
                factor = factor + 1
    return fact_list

def digits_sum(n):
    sum = 0
    while(n > 0):
        r = n % 10
        sum = sum + r
        n = n - r
        n = n // 10
    return sum

def add_all_digits(lst):
    sum = 0
    for i in range (len(lst)):
        sum += digits_sum(lst[i])
    return sum


def fun_nth_smithnumber(n):
    numbers = []
    for i in range(4,n + 1):
        fac = isfactor(i)
        print(fac)
        if len(fac) > 1:
            if digits_sum(i) == add_all_digits(fac):
                print(i)
    

print(fun_nth_smithnumber(0))
print(fun_nth_smithnumber(10))