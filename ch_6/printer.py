tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable(table):
	# Figure out length of longest string in each list
	colWidths = [0] * len(table)
	newList = []
	longest = ""
	for outer in table:
		for inner in range(len(outer)):
			if len(outer[inner]) > len(outer[inner-1]):
				longest = len(outer[inner])
		newList.append(int(longest))
	colWidths = newList

	
	# Sort columns and justify according to column width
	for outside in range(len(table[0])):
		for inside in range(len(table)):
			print(table[inside][outside].rjust(colWidths[inside]) + " " , end ="")
		print()


printTable(tableData)	


