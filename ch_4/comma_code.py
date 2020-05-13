def seperate(items):
	try:
		if len(items) == 1:
			print(str(items[0]))

		elif len(items) == 2:
			print(str(items[0]) + " and " + str(items[1]))	

		else:	
			# Isolate list items from last item
			minusLast = items[0:-1]
			sentence = ""
			
			# Add first items and last items to variable "sentence"
			for words in minusLast:
				sentence += str(words) + ", "
			sentence += "and " + str(items[-1])

			# Print variable
			print(sentence)

	except IndexError: 
		print("The list must have items!")


