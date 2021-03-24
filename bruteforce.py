from hashlib import sha256
from datetime import datetime

# Things to play with ##################################################################
showComps = False		# Show the sha 256 encrypts we are trying. Can be True or False.
showGuesses = False		# Show the raw password we are trying. Can be True or False.
asciiRangeMin = 33		# Numbers and Symbols (33), No special (48), lowercase only (97)
asciiRangeMin = 33		# Numbers and Symbols (33), No special (48), lowercase only (97)
asciiRangeMax = 122		# Remains 122, unless using complex characters
########################################################################################

startTime = datetime.now()


password = input('Password to Try to crack? ')

answer = sha256(password.encode('utf-8')).hexdigest()

passwordToTry = [chr(asciiRangeMin)]
line = ''
ops = 0
while sha256(str(line.join(passwordToTry)).encode('utf-8')).hexdigest()!=answer:

	if showComps == True:
		print(sha256(str(line.join(passwordToTry)).encode('utf-8')).hexdigest()+'!='+answer)
	
	cursor = 0
	flag = False
	while flag==False:
		passwordToTry[cursor]= chr(ord(passwordToTry[cursor])+1)
		if ord(passwordToTry[cursor])==asciiRangeMax+1:
			passwordToTry[cursor]= chr(asciiRangeMin)
			if len(passwordToTry)<=cursor+1:
				passwordToTry.append(chr(asciiRangeMin))
				flag = True
			else:
				cursor+=1
		else:
			flag = True
	ops+=1
	if showGuesses == True:
		print(line.join(passwordToTry))

endTime = datetime.now()
print('We have a match! The password was '+str(line.join(passwordToTry))+' It took '+str(ops)+' brute force guesses! ('+str(endTime-startTime)+')')

print(sha256(str(line.join(passwordToTry)).encode('utf-8')).hexdigest()+'=='+answer)
