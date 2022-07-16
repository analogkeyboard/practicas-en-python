
lista=[]
suma=0
limite=int(input("introduce el tamano de la lista: "))
for i in range(0,limite+1):
    if i %2 == 0:
        lista.append(i)
        suma=suma+i
print("lista: ",lista)
print("suma de los numeros en la lista:",suma)


 