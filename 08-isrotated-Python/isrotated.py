# isRotated(str1, str2) [10 pts]
# Write an efficient program to test if two given String is a rotation of each other or not, e.g. 
# if given String is "XYZ" and "ZXY" then your function should return true, but if the input is 
# "XYZ" and "YXZ" then return false.
def rotate(input,d): 
    # slice string in two parts for left and right 
    Lfirst = input[0 : d] 
    Lsecond = input[d :] 
    Rfirst = input[0 : len(input)-d] 
    Rsecond = input[len(input)-d : ] 
    return (Lfirst+Lsecond)



def isrotated(str1, str2):
	for i in range(len(str1)):
		d = rotate(str1,i)
		if(d == str2):
			return True
	return False

print(isrotated("XYZ","ZXY"))