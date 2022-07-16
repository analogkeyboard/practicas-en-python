print("Programa que lee las lineas  en un fichero de texto existente")

leer_fichero=open("fichero1.txt","r")
# fichero.write("Primer linea\n")
for linea in leer_fichero:
    print(linea,end='')

# fichero.write("Tercera linea\n")

leer_fichero.close()