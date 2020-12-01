i = 236491
#print(str(i)[0:2])
#It is a six-digit number. **
#The value is within the range given in your puzzle input. **
#Two adjacent digits are the same (like 22 in 122345).
#Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
def adjacentEqual(num):
	s = str(num)
	for i in range(0,5):
		if int(s[i:i+2]) % 11 == 0:
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

while i <= 713787:
	i += 1
	if not(adjacentEqual(i)) or not(assendingDending(i)):
		continue
	somme += 1

print(somme)
