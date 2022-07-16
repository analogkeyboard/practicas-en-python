import re
#Ejemplo 2.-aqui ya no se cumple la condicion ya que 'cadenaa' cuenta con 7 letras y 'cadena' solo con 6
#aun si ambas cadenas tienen la misma palabra la longitud de la primera palabra es mayor que la segunda
if re.match("cadenaa","cadena"):
	print("La cadena coincide")
else:
	print("No coinciden")
