# longestDigitRun(n) [20 pts]
# Write the function longestDigitRun(n) that takes a possibly-negative int value n and returns 
# the digit that has the longest consecutive 
# run, or the smallest such digit if there is a tie. So, longestDigitRun(117773732) returns 7 (
# because there is a run of 3 consecutive 7's), 
# as does longestDigitRun(-677886).
import collections

def get_key(val,freq): 
    for key, value in freq.items(): 
         if val == value: 
             return key 

def longestdigitrun(n):
	d = collections.defaultdict(int)
	b = str(abs(n))
	repeat = b[0]
	b = b[1:]
	count = 1
	for item in b:
		if item != repeat:
			print(repeat)
			if(repeat in d):
				if(d[repeat] < count):
					d[repeat] = count
			else:
				d[repeat] = count
			count = 1
			repeat = item
		else:
			count += 1
	l = list(d.items())
	l.sort()
	d = dict(l)
	m = max(d.values())
	print(d)
	return int(get_key(m,d))

print(longestdigitrun(44332211))