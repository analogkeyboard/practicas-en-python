import os
import sys


def texto_menu():
	print("Programa de creacion de tablas de multiplicar\n\n")
	
	print("*"*50)
	print("Directorio Actual: "+os.getcwd())
	print("\nSelecciona una opcion")
	print("1.-Nuevo archivo")
	print("2.-Abrir archivo")
	print("3.-Mostrar archivos")
	print("4.-Abrir directorio actual")
	print("5.-Salir")
	print("*"*50)
	


def menu_loop():
	try:
		while True:
			opciones()
	except EOFError as e:
		print("Programa Finalizado con CTRL+Z")

	except KeyboardInterrupt as e:
		print("Programa Finalizado con CTRL+C")
	
	finally:
		print("Programa Terminado Manualmente")


def opciones():

	texto_menu()
	try:
		opcion=int(input("\nOpcion: "))

		if opcion==1:
			limpiarPantalla()
			nuevoArchivo()
			
		elif opcion==2:
			limpiarPantalla()
			abrir_archivo()

		elif opcion==3:
			listar_archivos()
			limpiarPantalla()

		elif opcion==4:
			limpiarPantalla()
			comando_abrir_directorio_actual()

		elif opcion==5:
			print("Programa Finalizado")
			sys.exit()
			# menu_loop()

		else:
			print("Opcion Invalida")

	except ValueError as e:
		print("Opcion Invalida")

		
def nuevoArchivo():

	texto_menu()
	print("\nCreacion de tabla de multiplicar\n")

	entrada_tabla=int(input("Ingresa la tabla que quieres imprimir: "))
	numero_maximo=int(input("Ingresa hasta que numero quieres la tabla: "))
	guardar=input("Guardar archivo como: ")
	nombre_archivo=guardar+".txt"
	crea_tabla(entrada_tabla,numero_maximo,nombre_archivo)


def crea_tabla(tabla,num_max,nombre_archivo):
	with open(nombre_archivo, "w") as f:

		f.write("Tabla de multiplicar\n")

		for x in range(1,num_max+1):

			m=tabla*x

			print(str(tabla),"x",x,"=",m)

			f.writelines(str(tabla)+"x"+str(x)+"="+str(m)+"\n")
	comando_pause()
	limpiarPantalla()

def abrir_archivo():
	comando_dir()
	
	print("\nQue documento desea abrir?")
	file=input("Nombre del Archivo: ")
	file="\""+file+"\""
	os.system('type'+" "+file)
	os.system('notepad'+" "+file)
	limpiarPantalla()


def listar_archivos():
	print("\nLista de Archivos Disponibles\n")
	comando_dir()
	comando_pause()

def comando_pause():
	os.system('pause')
	
def limpiarPantalla():
	os.system('cls')

def comando_dir():
	os.system('dir')

def comando_abrir_directorio_actual():
	os.system('start.')

limpiarPantalla()
menu_loop()

