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
    while(n):
        r = n % 10
        sum = sum + r
        n = n // 10
    return sum

def is_smithnumber(n):
    l = isfactor(n)
    s1 = digits_sum(n)
    s2 = 0
    for i in range(len(l)):
        s2 += digits_sum(l[i])
    if(s1 == s2):
        return True
    else:
        return False

def fun_nth_smithnumber(n):
    if(n == 0):
        return 4
    s = 5
    count = 1
    while(count <= n):
        if(is_smithnumber(s)):
            count = count + 1
            if(n == count):
                break
        else:
            s = s + 1
    return s
print(fun_nth_smithnumber(0))
print(fun_nth_smithnumber(1))