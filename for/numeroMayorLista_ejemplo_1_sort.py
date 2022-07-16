#imprimir el mayor numero en una lista
#forma 1

lista1=[]
tam=int(input("tamano de la lista: "))

for item in range(tam):
	elem=int(input("introduce un numero: "))
	lista1.append(elem)

print("lista sin orden: ",lista1)
lista1.sort()
print("lista ordenada: ",lista1) 
print("el elemento mayor: ",lista1[-1])