# Write the function nthTidyNumber that takes a non-negative int n and returns the nth Tidy Number. 
# A tidy number is a number whose digits are in non-decreasing order.
# fun_nth_tidynumber(0) = 1
# fun_nth_tidynumber(1) = 2
# fun_nth_tidynumber(5) = 6
# fun_nth_tidynumber(15) = 17
# fun_nth_tidynumber(35) = 46
def isTidy(num):
    p = 10
    while(num):
        rem = num % 10
        num /= 10
        if rem > p:
            return False
        p = rem
    return True
def fun_nth_tidynumber(n):
    count = 0
    t = 1
    while(count <= n):
        print("t",t,count)
        if(isTidy(t)):
            count = count + 1
            if(count == n):
                return t
            else:
                t = t + 1
        else:
            print("divya")
            t = t + 1

print(fun_nth_tidynumber(15))