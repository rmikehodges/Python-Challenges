# This takes a text file and determines the odd lettered palidromes

def findOddPalindrome(word):
	placeholders = []
	middleIndex = (len(word)/2)
	if len(word)%2 != 0:
		for i in range(middleIndex):
			placeholders.append(word[i])
		for x in range(middleIndex + 1,len(word)):
			if placeholders[x-((x-middleIndex)*2)] != word[x]:
				return False
		return True
	else:
		return False

def parsePalindromes(inFile):
	holder = []
	corpus = open(inFile, "r")
	for line in corpus:
		if findOddPalindrome(line.rstrip()) == True:
			holder.append(line.rstrip())
	corpus.close()
	return holder

userInput = raw_input("Enter the name of the file that contains the text: ")
#print findOddPalindrome("mesosomes")
print len(parsePalindromes(userInput))	
