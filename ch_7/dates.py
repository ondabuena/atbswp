import re

#ask date
date = input("Give me a date in the form DD/MM/YYYY: ")

#compile regex DD/MM/YYYY
dateRegex = re.compile(r'(\d{2})/(\d{2})/([0-9]+)')
dateCheck = dateRegex.search(date)

#set variables and sort months according to no. days
day = dateCheck.group(1)
month = dateCheck.group(2)
year = dateCheck.group(3)
days30 = ["04", "06", "09", "11"]
days31 = ["01", "03", "05", "07", "08", "10", "12"]
days28 = ["02"]

#check validity of feb dates
if month in days28:
	if int(year) % 4 == 0 and int(day) > 29:
		print(f"Month {month} has 29 days in a leap year!")
	elif int(year) % 4 != 0 and int(day) > 28:	
		print(f"Month {month} should have less than 28 days!" )	
	else:
		print("That's a valid date.")	
#check validity of other dates
else:	
	if month in days30 and int(day) > 30:
		print(f"Month {month} should have less than 30 days!" )
	elif month in days31 and int(day) > 31:
		print(f"Month {month} should have less than 31 days!" )
	elif int(month) > 12:
		print("There are only 12 months in a year!") 
	elif  not 1000 <= int(year) < 2999:
		print("Please pick a year between 1000 and 2999.")
	else:
		print("That's a valid date.")


