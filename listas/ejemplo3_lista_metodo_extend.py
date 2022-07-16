print("Metodo extend()")
lista1=[]
lista2=[2,3,5]
print("Lista 1 original: ",lista1)
print("Lista 2 : ",lista2)
print("\n")

datos=int(input("¿Cuantos elementos quieres agregar?: "))
for x in range(datos):
    x=x+1
    n=int(input("Introduce el numero["+str(x)+"]: "))
    lista1.append(n)

print("\nLista 1 con elementos agregados: ",lista1)
lista1.extend(lista2)
print("\nLista 1 con los elementos agregados de la lista 2: ",lista1)