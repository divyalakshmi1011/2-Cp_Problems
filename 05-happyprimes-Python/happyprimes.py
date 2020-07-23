# Happy Primes [20 pts]
# Background: read the first paragraph from the Wikipedia page on happy numbers. After 
# some thought, we see that no matter what number we start with, when we keep replacing 
# the number by the sum of the squares of its digits, we'll always either arrive at 4 (
# unhappy) or at 1 (happy). With that in mind, we want to write the function nthHappyNumber
# (n). However, to write that function, we'll first need to write isHappyNumber(n) (
# right?). And to write that function, we'll first need to write sumOfSquaresOfDigits(n). 
# And that's top-down design! Here we go.... 
# Note: the autograder will grade each of the following functions, so they are required. 
# However, they also are here specifically because they are just the right helper 
# functions to make nthHappyNumber(n) easier to write!

def prime(n): 
	return all([(n % j) for j in range(2, int(n**0.5)+1)]) and n>1

def ishappyprimenumber(n):
    # Your code goes here
    s = str(n)
    if(n == 1):
        return True
    if(len(s) == 1 or n < 0):
        return False
    while(len(s) > 1 and prime(n)):
        sum = 0
        for i in range(len(s)):
            sum += (int(s[i]))**2
        s = str(sum)
        print("s",s)
    if(len(s) == 1):
        print(s)
        if(int(s) == 1):
            return True
    return False

print(ishappyprimenumber(833))
print(prime(833))