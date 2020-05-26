import re

#open file
madFile = open('./libsMad.txt')
fileRead = madFile.read()

#parse file for key word types
wordRegex = re.compile(r'NOUN|VERB|ADJECTIVE')
mo = wordRegex.findall(fileRead)

#take input and replace 
for m in mo:
	if m == "ADJECTIVE":
		inpt = input("Enter an %s: " %m)
	else:
		inpt = input("Enter a %s: " %m)	

	fileRead = wordRegex.sub(inpt, fileRead, 1)

#write over file and print to console
madFile = madFile = open('./libsMad.txt', 'w')
madFile.write(fileRead)
madFile.close()
print(fileRead)