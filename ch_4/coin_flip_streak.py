import random

numberOfStreaks = 0
for experimentNumber in range(10000):
	results = []
	streak = 0

	# Code that creates a list of 100 'heads' or 'tails' values.
	for i in range(100):
		i = random.randint(0,1)
		results.append(i)
		
	# Code that checks if there is a streak of 6 heads or tails in a row.
	for r in range(len(results)):
		if results[r] == results[r-1]:
			streak += 1
		else: 
			streak = 1	
		if streak == 6:
			numberOfStreaks += 1
			streak = 0

print('Chance of streak: %s%%' % (numberOfStreaks / 10000))			
print(numberOfStreaks)

