# isRotated(str1, str2) [10 pts]
# Write an efficient program to test if two given String is a rotation of each other or not, e.g. 
# if given String is "XYZ" and "ZXY" then your function should return true, but if the input is 
# "XYZ" and "YXZ" then return false.


def isrotated(str1, str2):
	l = len(str1)
	r = str1[::-1]
	for i in range(l):
		a = r[i]
		b = str1[:i]
		c = str1[i + 1:]
		print(a,b,c)
		if(a+c+b == str2):
			return True
	return False


print(isrotated("XYZ","ZXY"))