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
	# your code goes here
	x = inches//36
	if(x == 0):
		return 1
	return x

def fun_fabricexcess(inches):
	# your code goes here
	y = fun_fabricyards(inches)
	z = y*36
	if(z > inches):
		return z - inches
	elif(z == inches):
		return 0

print(fun_fabricyards(108))
print(fun_fabricexcess(100))
