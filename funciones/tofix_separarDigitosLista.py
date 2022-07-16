
lista=[]
def numero_cadena(dato):
    for i in dato:
        print("debug:",i)
        lista.append(int(i))
        print(lista[:])
        
    print(lista)

datos=int(input("dame un numero: "))
numero_cadena(datos)
