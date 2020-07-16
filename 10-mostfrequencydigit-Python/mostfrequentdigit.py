# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.


def get_key(val,freq): 
    for key, value in freq.items(): 
         if val == value: 
             return key 

def mostfrequentdigit(n):
	# Creating an empty dictionary
    my_list = [int(x) for x in str(n)] 
    freq = {} 
    for item in my_list: 
        if (item in freq): 
            freq[item] += 1
        else: 
            freq[item] = 1
    x = max(freq, key=freq.get)
    return get_key(x,freq)

print(mostfrequentdigit(11223344))