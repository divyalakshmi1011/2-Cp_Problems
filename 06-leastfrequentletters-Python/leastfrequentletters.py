# leastFrequentLetters(s) [20 pts]
# Write the function leastFrequentLetters(s), that takes a string s, and ignoring case (so "A" and "a" are treated 
# the same), returns a lowercase string containing the least-frequent alphabetic letters that occur in s, each 
# included only once in the result and then in alphabetic order. So:
# leastFrequentLetters("aDq efQ? FB'daf!!!") 
# returns "be". Note that digits, punctuation, and whitespace are not letters! Also note that seeing as we have not 
# yet covered lists, sets, maps, or efficiency, you are not expected to write the most efficient solution. Finally, 
# if s does not contain any alphabetic characters, the result should be the empty string ("")

def leastfrequentletters(s):
	s = s.replace(" ","")
	s = s.lower()
	d = {}
	for i in s:
		if i.isalpha():
			if i not in d:
				d[i] = 1
			else:
				d[i] += 1
	l = list(d.values())
	m = min(l)
	y =""
	for key, value in d.items(): 
		if m == value: 
			y += key

leastfrequentletters("aDq efQ? FB'daf!!!")
