i = 156217
#print(str(i)[0:2])
#It is a six-digit number. **
#The value is within the range given in your puzzle input. **
#Two adjacent digits are the same (like 22 in 122345).
#Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
def adjacentEqual(num):
	s = str(num)

	for i in range(0,5):
		left = False
		right = False
		if int(s[i:i+2]) % 11 == 0:
			if i != 0:
				if int(s[i-1:i+2]) % 111 == 0:
					continue
				else:
					left = True
			if i != 4:
				if int(s[i:i+3]) % 111 == 0:
					continue
				else:
					right = True
			if right and left:
				return True				
			if i == 0 and right:
				return True
			if i == 4 and left:
				return True
	return False


def assendingDending(num):
	s = str(num)
	mini = int(s[0])
	for i in range(1,6):
		if int(s[i]) < mini:
			return False
		else :
			mini = int(s[i])
	return True
somme = 0
#breakpoint()
print(adjacentEqual(112233))
print(adjacentEqual(123444))
print(adjacentEqual(111122))
while i <= 652527:
	i += 1
	if not(adjacentEqual(i)) or not(assendingDending(i)):
		continue
	somme += 1

print(somme)