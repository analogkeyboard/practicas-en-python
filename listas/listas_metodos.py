#declaracion de una lista vacia
lista = []
print("lista vacia",lista)

#lista con datos int
lista2=[1,2,3]
print("lista con datos",lista2)

#lista con datos int , float y booleanos
lista3=[1,"cadena",5.2,True,False]
print("lista con datos mixtos",lista3)

#metodos para la lista
#agregar un elemento al final de la lista
lista4=[1,3,5]
lista4.append(6)
print(lista4)

#copiar lista 
listaCopia=lista4.copy()
print(listaCopia)

#limpiar la lista
listaCopia.clear()
print(listaCopia)

#contar cuantas veces se repite un elemento
#dentro de una lista
listaConValoresRepetidos=[1,1,3,4]
print(listaConValoresRepetidos.count(1))

#contar cuantos elementos tiene el elemento
listaLargo=[1,2,3,4,5]
print(len(listaLargo))

#accediendo a un elemento en esspecifico
#mediante el indice
listaPalabras=["hola","mundo","!"]
print(listaPalabras[1])

#eliminar el primer elemento de una lista o por el valor del elemento
lista5=[1,"cadena",5]
print(lista5)
lista5.remove(1)
print(lista5)

#eliminar el ultimo elemento de una lista
lista5.pop()
print(lista5)

#accediendo a los elementos de la lista
lista6=["hola","mundo",4,5,6]
print("elemento: ",lista6[2])

#imprimir lista en orden inverso
lista7=[1,2,3,4,5]
lista7.reverse()
print(lista7)

lista8=[4,6,7,1]
lista9=['4',6,7,1]
lista8.sort()
print(lista8)

