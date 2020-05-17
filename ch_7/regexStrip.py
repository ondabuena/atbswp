import re

def regexStrip(string, remove=''):
	if remove:
		remover = re.sub(remove + ' ' , '', string)
		print(remover)	

	else:
		strip = re.compile(r'(^\s+)|(\s+$)')
		stripped = strip.sub('', string)
		print(stripped)
	


