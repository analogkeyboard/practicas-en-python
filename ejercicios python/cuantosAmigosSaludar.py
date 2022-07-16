lista=[]
numero=int(input("Cuantos amigos quieres: "))

def pideAmigos():
    for i in range(numero):
        nombre=input("dame nombre: ")
        lista.append(nombre)

def mostrarLista():
    for i in lista:
        print("amigo:",i)

pideAmigos()
mostrarLista()
