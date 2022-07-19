def busqueda_lineal(lista,x):
	i=1

	for z in lista:
		if z==x:
			print("iteraciones:",i)
			return "tamaño de la lista: ",len(lista)
		i=i+1

	return -1

print(busqueda_lineal([13,23,24,34,35,36,38,42,47,51,68,74,75,85,97,99],99 ))