lista=[]
def entrada5amigos():
    for i in range(5):
        dato=input("Introduce un nombre: ")
        i=dato
        lista.append(i)
    
def imprimerListaAmigos():
    for i in lista:
        print("\nHola!:",i)

entrada5amigos()
imprimerListaAmigos()
    
