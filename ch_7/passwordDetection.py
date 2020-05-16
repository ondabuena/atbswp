import re


while True:
	#Takes password input/compiles regex
	password = input("Enter a password: ")
	digitRegex = re.compile(r'\d+')
	digitCheck = digitRegex.search(password)
	letRegex = re.compile(r'[A-Z]+[a-z]+')
	letCheck = letRegex.search(password)

	#length check
	if len(password) < 8:
		print("Password must be at least 8 characters long.")

	#regex to check for digits:	
	elif not digitCheck:
		print("Password must contain at least a number.")	

	#regex to check for letter cases
	elif not letCheck:
		print("Password must contain both lowercase and uppercase letters")

	else:
		print("Password successfully entered.")
		break




