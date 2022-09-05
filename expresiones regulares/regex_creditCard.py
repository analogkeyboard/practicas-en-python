import re

patron_cuenta=r"^\d{4}\s\d{4}\s\d{4}\s\d{4}$"
patron_fecha=r"^(\d{1,2})/(\d{1,2})/(\d{4})$"
patron_pin_secreto=r"^\d{3}$"

cuenta="1111 2222 3333 4444"
fecha="13/20/2000"
pin="123"

regex1=re.search(patron_cuenta,cuenta)
regex2=re.search(patron_fecha,fecha)
regex3=re.search(patron_pin_secreto,pin)

if regex1 and regex2 and regex3:
	print("cuenta:",cuenta)
	print("fecha:",fecha)
	print("pin:",pin)
else:
	print("Patron no encontrado")