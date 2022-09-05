def suma(n):
	""" 
	multiplica el elemento entero del iterable por 2

	"""
	return n*2

numeros=[1,2,5,7,3,1,0,20]

help(suma)
print(numeros)
print(list(map(suma,numeros)))
