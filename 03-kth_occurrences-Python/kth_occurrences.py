# Given a string str and an integer K, the task is to find the K-th most 
# frequent character in the string. If there are multiple characters that 
# can account as K-th the most frequent character then, print any one of them.



def fun_kth_occurrences(s, n):
	s = s.strip()
	my_list = list(s)
	freq = {} 
	for item in my_list: 
		if (item in freq): 
			freq[item] += 1
		else: 
			freq[item] = 1
			x = []
	l = list(freq.values())
	m = list(freq.keys())
	l.sort(reverse = True)
	p = list(freq.values())
	print("l",l)
	for i in l:
		print("i",i)
		t = m[p.index(i)]
		print("t",t)
		x.append(t)
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
	return x[0]

print(fun_kth_occurrences("    h  ", 2))
