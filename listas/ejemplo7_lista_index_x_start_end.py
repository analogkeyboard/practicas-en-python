
print("Regresar un elemento de la lista")
lista=[1,2,3,4,5,6,7,8,9,10]
print("Lista: ",lista)

i=0

for x in lista:
    print("lista["+str(i)+"]=",str(x))
    i=i+1
    
elemento=int(input("Que elemento deseas encontrar: "))
start=int(input("indice inicio: "))
end=int(input("indice final: "))


print("El elemento retornado esta en la posicion: ",lista.index(elemento,start,end))