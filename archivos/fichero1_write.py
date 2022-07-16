print("Programa que escribe 3 lineas en un fichero de texto existente")

fichero=open("fichero1.txt","w")
fichero.write("Primer linea\n")
fichero.write("Segunda linea\n")
fichero.write("Tercera linea\n")

fichero.close()