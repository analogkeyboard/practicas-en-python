tabla_archivo=int(input("Ingresa la tabla: "))
tabla_linea=int(input("Ingresa la linea que quieres imprimir: "))
# n=7
# m=4
nombre="tabla-"+str(tabla_archivo)+".txt"
try:
	with open(nombre,"r") as fichero:
		# print(fichero.read())
		numero_linea=0
		for x in fichero:
			if numero_linea==tabla_linea:	
				print("\n"+x)
			numero_linea=numero_linea+1
except FileNotFoundError:
	print("\nArchivo no encontrado")