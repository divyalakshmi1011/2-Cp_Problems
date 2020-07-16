# A Caesar Cipher is a simple cipher that works by shifting each letter in 
# the given message by a certain number. For example, if we shift the message 
# "We Attack At Dawn" by 1 letter, it becomes "Xf Buubdl Bu Ebxo"
# Write the function applyCaesarCipher(message, shift) which shifts the given 
# message by shift letters. You are guaranteed that message is a string, and 
# that shift is an integer between -25 and 25. Capital letters should stay capital 
# and lowercase letters should stay lowercase, and non-letter characters should not be changed. 
# Note that "Z" wraps around to "A". So, for example:
# assert(applyCaesarCipher("We Attack At Dawn", 1) == "Xf Buubdl Bu Ebxo")
# assert(applyCaesarCipher("zodiac", -2) == "xmbgya")


def fun_applycaesarcipher(msg, shift):
	s = 'abcdefghijklmnopqrstuvwxyz'
	s1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	t = ''
	for i in range(len(msg)):
		if(msg[i] in s):
			index = s.index(msg[i])
			if(shift > 0):
				if(msg[i] == 'z'):
					t += 'a'
				else:
					t += s[index + shift]
			elif(shift < 0):
				if(msg[i] == 'a'):
					f = s[::-1]
					t += f[abs(shift + 1)]
				else:
					print(i,shift)
					t += s[index + shift]
		else:
			t += msg[i]
	return t

print(fun_applycaesarcipher("zodiac",-2))


