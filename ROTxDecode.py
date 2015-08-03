#Simply ROT decryption program

UpperIndex = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
LowerIndex = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def RotateString(rotationNum, letterList):
	newList = [i for i in range(26)]
	for i in range(0,26):
		if ((i+rotationNum) > 25):
			newList[i] = letterList[(i+rotationNum)-26]
		else:
			newList[i] = letterList[i+rotationNum]
	return newList

def decodeString(input, LowerList, UpperList):
	decoded = ""
	for i in range(len(input)):
		if input[i] in UpperList:
			decoded+=UpperList[UpperIndex.index(input[i])]
		if input[i] in LowerList:
			decoded+=LowerList[LowerIndex.index(input[i])]
		if input[i] == " ":
			decoded+=" "
	return decoded

theString = raw_input("Enter the string you wish to rotate: ")
rotation = int(raw_input("Enter the number you wish to rotate: "))

print "Your rotated string is " + decodeString(theString, RotateString(rotation,LowerIndex), RotateString(rotation, UpperIndex))	
