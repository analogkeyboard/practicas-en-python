import re
cadena=0
patron=r"^\d{0,6}$"
regex=re.search(patron, str(cadena))
if regex:
	print("el patron es correcto")
else:
	print("el patron es incorrecto")
