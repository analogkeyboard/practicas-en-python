"""
archivo=open("chanchito.txt")

#archivo.write("una nueva linea")
#archivo.write("\nuna nueva linea")

print(archivo.read())

archivo.close()
"""

import os

if os.path.exists("chanchito2.txt"):
    os.remove("chanchito2.txt")
else:
    print("el archivo no existe")