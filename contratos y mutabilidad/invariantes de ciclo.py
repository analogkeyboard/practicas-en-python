def maximo(lista):
	if not len(lista):
		return None
	max_elem=lista[0]
	for elemento in lista:
		if elemento > max_elem:
			max_elem=elemento
	return max_elem

mi_lista=[1,5,6,9]
print("Lista:",mi_lista)
print("Elemento Maximo de la lista:",maximo(mi_lista))

def potencia(b,n):
	p=1
	for i in range(n):
		p*=b
	return p

print("Pontencia de un numero:",potencia(5,3))

def suma(b,n):
	suma=0
	for i in range(b,n):
		suma=suma+i
	return suma

print("La suma es:",suma(1,10))
#1 2 3 4 5 6 7 8 9 