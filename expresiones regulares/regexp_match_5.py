import re

cadena="cola"
regex="hola|cola|sola"
if re.match(regex,cadena):
	print("La cadena",cadena,"coincide con",regex)
else:
	print("No coinciden")