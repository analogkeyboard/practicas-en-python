#las expresiones regulares sirven para encontrar o definir patrones en una cadena
#para ellos importamos la libreria 're'
import re

#	--------------match(expresion,comparacion)-------------

#Le pasamos como parametro una cadena y la cadena con la que queremos compararla

#Ejemplo 1.-comparamos cadena con cadenaa
#si coinciden se mostrara el mensaje del if en caso contrario mostrara la de else
#en este ejemplo muestra que si coincide porque 'cadena' si se encuentra dentro de 'cadenaa'
if re.match("cadena","cadenaa"):
	print "La cadena coincide"
else:
	print "No coinciden"


#Ejemplo 2.-aqui ya no se cumple la condicion ya que 'cadenaa' cuenta con 7 letras y 'cadena' solo con 6
#aun si ambas cadenas tienen la misma palabra la longitud de la primera palabra es mayor que la segunda
if re.match("cadenaa","cadena"):
	print "La cadena coincide"
else:
	print "No coinciden"

#	--------------match(.expresion,comparacion)-------------
#Ejemplo 3.- Aqui utilizamos el caracter punto (.)
#El punto nos indica que puede iniciar con un caracter cualquiera, en este caso .ython nos dice que podemos
#escribir python,mython,jython etc. porque se cumple con lo que sigue despues del punto que seria 'ython'

if re.match(".ython","python"):
	print "La cadena coincide"
else:
	print "No coinciden"

#Ejemplo 4.- en este caso la cadena es'python.com' , esta cadena al contener un punto tenemos que utilizar
#una barra invertida para que ignore el punto y utilize el punto de la cadena 'pytho.'
if re.match("pytho.\.com","python.com"):
	print "La cadena coincide"
else:
	print "No coinciden"

cadena="cola"
regex="hola|cola|sola"
if re.match(regex,cadena):
	print "La cadena",cadena,"coincide con",regex
else:
	print "No coinciden"