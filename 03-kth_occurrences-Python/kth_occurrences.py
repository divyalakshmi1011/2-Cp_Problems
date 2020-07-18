# Given a string str and an integer K, the task is to find the K-th most 
# frequent character in the string. If there are multiple characters that 
# can account as K-th the most frequent character then, print any one of them.



def fun_kth_occurrences(s, n):
	my_list = list(s)
	freq = {} 
	for item in my_list: 
		if (item in freq): 
			freq[item] += 1
		else: 
			freq[item] = 1
	maxi = max(freq.values())
	x = []
	for item in freq.keys():
		if(maxi == freq[item]):
			x.append(item)
	print(x)
	count = 0
	for i in range(len(x)):
		if(freq[x[i]] > 1):
			print(x[i])
			count = count + 1
		if(count == n):
			print(x)
			print(count,n)
			return x[i]
			break

print(fun_kth_occurrences("helllo woorld",2))
