import re
#Ejemplo 4.- en este caso la cadena es'python.com' , esta cadena al contener un punto tenemos que utilizar
#una barra invertida para que ignore el punto y utilize el punto de la cadena 'pytho.'
if re.match("pytho.\.com","python.com"):
	print("La cadena coincide")
else:
	print("No coinciden")