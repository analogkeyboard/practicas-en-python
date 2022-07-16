print("Metodo insert()\n")
lista=[1,2,3,5,6,8]
print("Lista 1 original: ",lista)

print()

i=0
print("Lista recorrida con sus posiciones: ")
for x in lista:

    print("Lista[",i,"]=",x)
    i=i+1
    
num_elementos=int(input("Cuanto elementos quiere insertar: "))
for x in range(num_elementos):
    x=x+1
    pos=int(input("\nIntroduce la posicion["+str(x)+"]: "))
    num=int(input("Introduce el valor: "))
    lista.insert(pos,num)
    print("Lista actualizada: ",lista,end="")   

print("\nLa lista con los valores insertados es: ",lista)    
