#encontrar el numero menor de una lista
lista=[1,5,6,-7,4]

menor='init'

for x in lista:
    if menor=='init':
        menor=x
        print(menor,x)
    else:
        menor = x if x < menor else menor
        print(menor,x)
print("menor",menor,x)