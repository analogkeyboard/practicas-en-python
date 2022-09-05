def numero_par(valor):
	"""
	Devuelve el numero par del iterable usando la funcion filter()
	"""
	return valor%2==0

lista=[0,3,4,5,6,8,9,10]

help(numero_par)
print(lista)
print(list(filter(numero_par,lista)))