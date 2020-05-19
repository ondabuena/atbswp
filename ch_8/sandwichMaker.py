import pyinputplus as pyip  

cost = {
	'bread': {
		"wheat": 2,
		"white": 1,
		"sourdough": 2,
	},
	'protein': {
		'chicken': 5,
		'turkey': 5,
		'ham': 4,
		'tofu': 4,
	},
	'cheese': {
		'cheddar': 2,
		'swiss': 3,
		'mozzarella': 3,
	},
	'extra': 1
	# 'extras': {
	# 	'tomato': 1,
	# 	'mustard': 1,
	# 	'mayo': 1,
	# 	'lettuce': 1,
	# },
}

tally = []
bread = pyip.inputMenu(["wheat", "white", "sourdough"])
tally.append(cost["bread"][bread])
protein = pyip.inputMenu(["chicken", "turkey", "ham", "tofu"])
tally.append(cost["protein"][protein])
cheese = pyip.inputYesNo("Would you like cheese?")
if cheese == 'yes':
	cheese = pyip.inputMenu(["cheddar", "swiss", "mozzarella"])
	tally.append(cost["cheese"][cheese])
else:
	cheese = "no cheese"	
extra = pyip.inputYesNo("Would you like extras?")
if extra == 'yes':
	extra = "extras"
else:
	extra = "no extras"	

print(f"We will make you a {protein} sandwich with {extra} and {cheese} on {bread} bread.")
print("your sandwich will cost: $" + str(sum(tally)))
