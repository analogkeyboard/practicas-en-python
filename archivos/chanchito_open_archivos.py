#se abre el archivo
#permisos:
#r: lectura
#r+: lectura y escritura
#w: sobreescritura, si no existe el archivo se creara
#a: anadir, escribe al final del archivo
#b: binario
#+: lectura y escritura simultanea
#U: salto de linea universal
#rb: lectura binario
#wb: sobreescritura binaria
#r+b: lectura y escritura binaria
chanchito=open("chanchito.txt")

#lee todo el archivo
#print(chanchito.read())

#lee una linea
"""
print(chanchito.readline())
print(chanchito.readline())
print(chanchito.readline())
print(chanchito.readline())
"""

#leer todo el archivo
for x in chanchito:
    print(x,end="")

chanchito.close()