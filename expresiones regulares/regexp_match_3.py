import re

#	--------------match(.expresion,comparacion)-------------
#Ejemplo 3.- Aqui utilizamos el caracter punto (.)
#El punto nos indica que puede iniciar con un caracter cualquiera, en este caso .ython nos dice que podemos
#escribir python,mython,jython etc. porque se cumple con lo que sigue despues del punto que seria 'ython'

if re.match(".ython","python"):
	print("La cadena coincide")
else:
	print("No coinciden")