# Write the function nthUglyNumber that takes a non-negative int n and returns the nth Ugly Number. 
# Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 
# 9, 10, 12, 15 shows the few ugly numbers. By convention, nthUglyNumber(0) will give 1.
def isprime(n):
    if n == 1:
        return False
    count = 0
    for i in range(1,n + 1):
        if(n % i == 0):
            count = count + 1
    if(count == 2):
        return True
    else:
        return False

def factors(n):
    l = []
    for i in range(1,n + 1):
        if(n % i == 0):
            if(isprime(i)):
                if( i == 3 or i == 5 or i == 2):
                    l.append(i)
    return l


def fun_nth_uglynumber(n):
    if n == 0:
        return 1
    count = 0
    u = 2
    while(count <= n):
        l = factors(u)
        if(len(l) > 0):
            count = count + 1
            if(count == n):
                break
            else:
                u = u + 1
        else: u = u + 1
    return u

print(fun_nth_uglynumber(10))