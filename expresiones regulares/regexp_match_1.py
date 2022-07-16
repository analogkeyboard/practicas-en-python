import re
#	--------------match(expresion,comparacion)-------------

#Le pasamos como parametro una cadena y la cadena con la que queremos compararla

#Ejemplo 1.-comparamos cadena con cadenaa
#si coinciden se mostrara el mensaje del if en caso contrario mostrara la de else
#en este ejemplo muestra que si coincide porque 'cadena' si se encuentra dentro de 'cadenaa'
if re.match("cadena","cadenaa"):
	print("La cadena coincide")
else:
	print("No coinciden")