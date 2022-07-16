#imprimir el mayor numero en una lista
#forma 2

lista1=[]
tam=int(input("tamano de la lista: "))

for item in range(tam):
	elem=int(input("introduce un numero: "))
	lista1.append(elem)

mayor=lista1[0]
print("debug mayor: ",lista1[0])

for item in lista1:
    if item > mayor:
        mayor=item
        print("debug 2 mayor: ",mayor)


print("El numero mayor: ",mayor)
 