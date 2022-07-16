#Abre el fichero si existe , si no entonces marca una exepcion
fichero=open("prueba.txt")
"""
for linea in fichero:
	linea=linea.rstrip()
	#print i," = ",linea
	print "%d: %s" % (i,linea)
	i+=

#fichero.close()
#print "\nFichero Cerrado"
"""

for i,linea in enumerate(fichero):
	linea=linea.rstrip("\n")
	#print i," = ",linea
	print i+1,":",linea
	

fichero.close()
print "\nFichero 2 Cerrado"