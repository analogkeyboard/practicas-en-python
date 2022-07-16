
import os
#fich = open("fichero.txt")
# ruta_fichero=os.path.join("pruebas","fichero.txt")
ruta_fichero=os.path.join("pruebas","fichero.txt")
fichero=open(ruta_fichero)
#lee todo el archivo
#leer=fichero.read()
#print(leer)

#lee cada linea cada vez que se invoca
"""
print(fichero.readline())
print(fichero.readline())
print(fichero.readline())
print(fichero.readline())
print(fichero.readline())
"""
#devuelve las lineas leidas como una lista
#print(fichero.readlines())

for linea in fichero:
    print(linea,end="")
