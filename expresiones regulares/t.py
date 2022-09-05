import re
cadena="02/1/2020"
regex=r"^(\d{1,2})/(\d{1,2})/(\d{4})$"
m=re.search(regex,cadena)
dia=int(m.group(1))
mes=int(m.group(2))
anio=int(m.group(3))
if m and (dia>0 and dia<32) and (mes>0 and mes<13) and (anio>1900 and anio<9999):
	print(m)
	print(m.group(1))
	print(re.findall(regex,cadena))
	print("Fecha ingresada correctamente")
else:
	print("patron no encontrado")
