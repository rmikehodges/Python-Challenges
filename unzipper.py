import zipfile
import os

#This needs some work
#1. make it able to find the zip file in the current one
#2. The make the new dir based on the name

def unzipIteration(fileNumber, pass2):
	fileBase = "/root/Downloads/PyNight/Hard6/"
	password = pass2
	for n in range(fileNumber, 0, -1):
		print n
		if not os.path.exists(fileBase + str(n)):os.makedirs(fileBase + str(n))
		myZipFile = fileBase  + str(n+1) + "/" + str(n) + ".zip"
		print myZipFile
		with zipfile.ZipFile(myZipFile, "r") as z:
			z.extractall(fileBase + str(n), z.namelist(), password)
		for subdir, dirs, files in os.walk(fileBase + str(n)):
			for thefile in files:		
				with open(os.path.join(subdir, thefile), 'r') as lookIn:
					for line in lookIn:
						if "KEY:" in line:
							password = line[4:].rstrip()

			

#make a list of zip file members and set it to variable

#iterate through members to find KEY: and set the variable

#store the key in a variable

#unlock the next set of zip files with the password and set the list variable

#decrement the variable

print unzipIteration(24, 'Gs0uZv')
