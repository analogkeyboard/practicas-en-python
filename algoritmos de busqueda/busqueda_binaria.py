print()

# lista=[2,3,5,10,27,30,34,51,65,77,81,82,93,99]
lista=[13,23,24,34,35,36,38,42,47,51,68,74,75,85,97,99]
# lista=[13,23,24,34,35,36,38,42,47,51,68,74,75,85,97,99]


print("Lista:",lista)

entrada=int(input("numero: "))
def busqueda_binaria(l,entrada):
	
	izquierda=0
	derecha=len(lista)-1

	if len(lista)%2==0:
		medio=(izquierda+derecha)//2
	elif len(lista)%2==1:
		medio=(izquierda+derecha+1)//2
	else:
		pass

	print("\nNumero de elementos:",len(lista))
	print("Indice desde 0 hasta",len(lista)-1)
	print("Primer Elemento:",lista[0])
	print("Ultimo Elemento:",lista[len(lista)-1])
	print("Elemento Izquierdo:",izquierda)
	print("Elemento Derecho:",derecha)
	print("Posicion media:",medio)
	print("Elemento de medio:",lista[medio])

	
	for x in lista:
		if entrada==lista[medio]:
			return 'posicion:',medio
			# print("iteracion:",i)
		elif entrada<lista[medio]:
			nueva_lista_izquierda=lista[:medio]
			print("\nLista actualizada:",nueva_lista_izquierda)
			medio=medio-1
			print("Nueva posicion medio:",medio)
			print("Elemento medio:",lista[((medio)//2)])
		
		else:
			nueva_lista_derecha=lista[medio+1:]
			print("\nLista actualizada:",nueva_lista_derecha)
			medio=medio+1
			print("Nueva posicion medio:",medio)
			print("Elemento medio:")

print(busqueda_binaria(lista, entrada))