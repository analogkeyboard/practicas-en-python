#para acceder a un elemento de la cadena
#utilizamoslos corchetes '[]' y dentro la posicion
#a la que queremos acceder

nombre="sakuray"

#si queremos acceder a la letra 'K' entonces
#contamos desde la posicion 0
#y seria la posicion 2

print "se muestra la letra: ",nombre[2]

#si quieres visualizar mejor la posicion
#puedes recorrer la cadena con un ciclo 'for'
#y mostramos la posicion con un contador

print "elementos recorridos con un ciclo for"
contador=0
for elemento in nombre:
	print "Posicion ["+str(contador)+"]="+str(elemento)
	#nota: podemos usar la forma abreviada
	#contador += 1
	contador=contador+1
	
	
#para acceder e imprimir todos los elementos de forma 'manual'
#se hace de la siguiente manera

print "elementos recorridos de forma manual"

print "Elemento 0: ",nombre[0]
print "Elemento 1: ",nombre[1]
print "Elemento 2: ",nombre[2]
print "Elemento 3: ",nombre[3]
print "Elemento 4: ",nombre[4]
print "Elemento 5: ",nombre[5]
print "Elemento 6: ",nombre[6]


	
