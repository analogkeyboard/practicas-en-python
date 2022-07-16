import os.path as fileexists

tabla=int(input("que tabla quiere abrir?: "))

nombre_archivo="tabla-"+str(tabla)+".txt"

try:
	with open(nombre_archivo,"r") as f:
		if fileexists(nombre_archivo):
			print("Archivo encontrado")

			for x in f.readlines():
				print(x,end="")
		
except FileNotFoundError:
	print("Archivo no encontrado")
