# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that 
# number contains two consecutive digits that are the same, and False otherwise.

def hasconsecutivedigits(n):
	# Store first digits as previous digit 
    prev_digit = n % 10
    n = int(n / 10) 
    res = prev_digit 
    # Iterate through all digits of n, note  
    # that the digits are processed from  
    # least significant digit to most  
    # significant digit. 
    while (n): 
        # Store current digit 
        curr_digit = n % 10
        if (curr_digit == prev_digit): 
            return True
        prev_digit = curr_digit 
        # Remove last digit from n 
        n = int(n / 10) 
    return False

print(hasconsecutivedigits(1266645))