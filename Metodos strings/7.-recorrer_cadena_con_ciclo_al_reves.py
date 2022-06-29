# -*- coding: utf-8 -*-

#la variable 'cadena' guarda nuestro string o texto
cadena="sakuray"

#guardamos el valor de el largo de la cadena de forma normal e inversa
#con normal me refiero que inicia desde el indice o posicion cero
#y con inversa es cuando inicia desde el primer indice negativo

#guarda el tamaño de la cadena , osea 7 elementos, desde el 0 al 6
largo_positivo=len( cadena)

#guarda el indice final de la cadena
ultimo_indice=len(cadena)-1

#guarda el tamaño de la cadena de forma negativa , osea desde -7 a -1
largo_negativo=-len( cadena)

#se guarda el indice -1 que siempre sera la posicion del ultimo elemento de la cadena en forma inversa
indice_negativo= -1

#se guarda el indice 0 , que siempre sera el primer elemento de la cadena de forma normal
indice_positivo=0


print "valor de la variable: ", cadena
print "numero de elementos de la cadena: ",largo_positivo
print "primer posicion de la cadena: ",indice_positivo
print "indice final de la cadena: ", ultimo_indice
print "primer posicion de la cadena inversa: ",indice_negativo
print "indice final de la cadena inversa ",largo_negativo

#print para dar un salto de linea
print

#creamos un titulo para cada columna, para mostrar ese efecto  utilizamos '\t', eso nos dara un espacio de tabulador, osea 4 espacios
print "ELEMENTO\t\tINDICE\t\t\t-INDICE"

#creamos un ciclo for para recorrer la cadena
#se lee , para todo elemento 'x' en la variable 'cadena'
for x in cadena:
	
	#luego imprimos 3 tablas
	#la primera es de los elementos de la cadena
	#la segunda muestra los elementos de la cadena pero accediendolos mediante su indice
	#la tercera hace lo mismo solo que de forma inversa
	
	print "elemento =",x,"\t\t","indice[",indice_positivo,"] = ",cadena[ indice_positivo],"\t\t","indice=[",largo_negativo,"] = ",cadena[indice_negativo]
	
	
	indice_positivo+=1
	indice_negativo-=1
	largo_negativo+=1
	
	


