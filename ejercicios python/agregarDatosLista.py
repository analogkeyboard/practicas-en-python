
lista=[]
def pedirDatos():
    dato=input("Ingresa un nombre: ")
    while dato!='*':
        lista.append(dato)
        #print("dato agregado: ",dato)
        print(lista)
        dato=input("Ingresa un nombre: ")

pedirDatos()