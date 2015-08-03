#Take a file with hex and output it as ascii

def convertHexFile(inFile, outFile):
	yourIn = open(inFile, "r")
	yourOut = open(outFile, "w")
	for line in yourIn:
		yourOut.write(line.decode("hex"))
	yourIn.close()
	yourOut.close()
	print "Your file has been written master..."

def findWordonLine(lineNum, wordNum, inFile):
	lines = []
	yourMom = open(inFile, "r")
	for line in yourMom:
		lines.append(line)
	theline = lines[lineNum-1].split()
	theWord = theline[wordNum-1]
	return "Word #"+ str(wordNum) + " on line #" + str(lineNum) +" is " + theWord
	

theOutFile = (raw_input("Enter the file you want to write to: "))
convertHexFile(raw_input("Enter the file you want to read from: ") ,theOutFile)

print findWordonLine(int(raw_input("Enter the line number you want to read: ")),int(raw_input("Enter the word number you want to read: ")),  theOutFile)

