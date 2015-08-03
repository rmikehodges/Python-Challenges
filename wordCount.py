#This will take two inputs from the user, the filename and the word to find

import re

def wordFind(word, theFile):
	regex = word + '[^\w]' #This regex searches the word with no following characters
	with open(theFile) as myFile:
		data="".join(line.rstrip().lower() for line in myFile)
	print len(re.findall(regex, data))

userWord = raw_input("Enter the word you're looking for: ")
userFile = raw_input("Enter the file you're looking in: ")
wordFind(userWord, userFile)

	
