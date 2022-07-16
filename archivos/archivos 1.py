#Abre el fichero si existe , si no entonces marca una exepcion
fichero=open("prueba.txt")

linea=None

#Lee cada linea del fichero de texto mientras no encuentre
#un caracter vacio
while linea!='':
	
	#Guarda cada cadena encontrara en el fichero
	linea=fichero.readline()

	#imprime cada cadena que encuentra la variable linea
	#la coma nos sirve para evitar el salto de linea , es decir lo
	#concatena , en este caso lo que concatena es el salto de linea
	print linea,

fichero.close()
print "\nFichero Cerrado"
