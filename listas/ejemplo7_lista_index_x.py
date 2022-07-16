
print("Regresar un elemento de la lista")
lista=[1,"hola",3,'4',5,6.0]
print("Lista: ",lista)

i=0

for x in lista:
    print("lista["+str(i)+"]=",str(x))
    i=i+1

print("¿Que tipo de dato deseas buscar?")

try:
    tipo_dato=input("(e)ntero,(f)lotante o (c)aracter/(c)adena?: ")
    if tipo_dato=='e':
        p=int(input("¿Que elemento deseas encontrar?: "))
    elif tipo_dato=='c':
        p=input("¿Que elemento deseas encontrar?: ")
    elif tipo_dato=='f':
        p=float(input("¿Que elemento deseas encontrar?: "))
    else:
        print("Opcion Invalida")

except NameError as e:
    print("El nombre de la variable no esta definido")

print("El elemento retornado esta en la posicion: ",lista.index(p))