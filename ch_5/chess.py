def isValidChessBoard(board):
	pieceCounter = []
	spaceCheck = []
	for v in board.values():
		pieceCounter.append(v)
	for k in board.keys():
		spaceCheck.append(k)

	white = whiteCheck(pieceCounter)
	black = blackCheck(pieceCounter)
	space = spaceValid(spaceCheck)
	pieces = pieceValid(pieceCounter)
	print(pieceCounter)
	if not white:
		print("Hmm, you have an invalid number of WHITE pieces on the board.")
	elif not black:
		print("Hmm, you have an invalid number of BLACK pieces on the board")
	elif not space:
		print("Hmm, you have entered an invalid space for your pieces")
	elif not pieces:
		print("Hmm, you have an invalid piece on the board")
	else:
		print("Looks like a valid chess board.")


def whiteCheck(pieceList):
	if len(pieceList) > 32:
		return False	
	elif "wking" not in pieceList:
		return False
	elif pieceList.count("wking") > 1:
		return False
	elif pieceList.count("wpawn") > 8:
		return False
	elif pieceList.count("wbishop") > 2:
		return False
	elif pieceList.count("wknight") > 2:
		return False
	elif pieceList.count("wrook") > 2:
		return False		
	elif pieceList.count("wqueen") > 1:
		return False
	else:	
		return True

def blackCheck(pieceList):
	if len(pieceList) > 32:
		return False	
	elif "bking" not in pieceList:
		return False
	elif pieceList.count("bking") > 1:
		return False
	elif pieceList.count("bpawn") > 8:
		return False
	elif pieceList.count("bbishop") > 2:
		return False
	elif pieceList.count("bknight") > 2:
		return False
	elif pieceList.count("brook") > 2:
		return False		
	elif pieceList.count("bqueen") > 1:
		return False
	else:	
		return True

def spaceValid(spaces):
	alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
	num = ["1", '2', '3','4','5','6','7','8']
	for space in spaces:
		if space[1] not in alph:
			return False
		elif space[0] not in num:
			return False			
	return True		

def pieceValid(pieces):
	availPieces = ["bpawn", "bbishop", "bknight", "brook", "bqueen", "bking", 
				"wpawn", "wbishop", "wknight", "wrook", "wqueen", "wking"]	
	
	for piece in pieces:
		if piece not in availPieces:
			return False
	return True
	




eg = {'1h': 'brook', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bking', '3e': 'wking',}
egg = {"1h": "bking", "6c": "wqueen", "2g": "bbishop", "5h": "bqueen", "3e": "wking"}
eggg = {"1a": "wking", "2a": "wking", "3c": "bbishop"}
egggg= {"1a": "bking", "9z": "wking"}
eggggg = {"1h": "bking", "6c": "wqueen", "2g": "bbishop", "5h": "bqueen", "3e": "wking", "4e": "january"}


isValidChessBoard(eg)
isValidChessBoard(egg)
isValidChessBoard(eggg)
isValidChessBoard(egggg)
isValidChessBoard(eggggg)

