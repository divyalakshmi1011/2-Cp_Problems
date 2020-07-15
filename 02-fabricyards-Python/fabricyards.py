# fabricyards(inches)
# Fabric must be purchased in whole yards, so purchasing just 1 inch 
# of fabric requires purchasing 1 entire yard. With this in mind, 
# write the function fabricYards(inches) that takes the number of 
# inches of fabric desired, and returns the smallest number of whole 
# yards of fabric that must be purchased.

# fabricexcess(inches)
# Write the function fabricExcess(inches) that takes the number of 
# inches of fabric desired and returns the number of inches of excess 
# fabric that must be purchased (as purchases must be in whole yards)
# . Hint: you may want to use fabricYards, which you just wrote!


def fun_fabricyards(inches):
	if(inches == 0):
		return 0
	# your code goes here
	x = inches/36
	s = str(x)
	l = s.split(".")
	print("l",l)
	if(int(l[0]) == 0):
		return 1
	else:
		if(int(l[1]) != 0):
			return int(l[0]) + 1
		else:
			return int(l[0])

def fun_fabricexcess(inches):
	# your code goes here
	if(inches == 0):
		return 0
	y = fun_fabricyards(inches)
	z = y*36
	print(z)
	if(z > inches):
		return z - inches
	elif(z == inches):
		return 0

print(fun_fabricyards(0))
print(fun_fabricexcess(0))
