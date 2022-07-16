def contadorPalabras(palabra):
	palabra_separada=palabra.split()
	print("\nPalabra Original: "+palabra)
	i=0
	print()
	for x in palabra_separada:
		# print(x)	
		if len(x)>5:
			i=i+1
	print(palabra_separada)
	print("\nNumero de palabras mayores a 5 letras: ",i)

	


contadorPalabras("palabras contadas con paciencia y coraje entre otras cosas perdidas")