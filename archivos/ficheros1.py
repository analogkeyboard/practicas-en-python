import io

texto="Una linea con texto\nOtra linea con texto"
fichero = io.open('fichero.txt','w')
fichero.write(texto)
fichero.close()

fichero2=open("fichero2.txt","r")
#texto=fichero2.read()
lineas=fichero2.readlines()
#print(texto)
print(lineas)
fichero2.close()

with open("fichero3.txt","r") as fichero3:
    for linea in fichero3:
        print(linea)

