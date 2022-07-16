tabla=int(input("tabla?: "))

nombre= "tabla-"+str(tabla)+".txt"

with open(nombre, "w") as f:

	for x in range(11):

		m=tabla*x
		f.writelines(str(tabla)+"x"+str(x)+"="+str(m)+"\n")
	print("Archivo "+nombre+" creado con exito")
		