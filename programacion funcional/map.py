def minuscula(t):
	""" 
	convierte el elemento iterable a minusculas

	"""
	return t.lower()

cadena=["HOLA","mUNdo","AdiOS"]

help(minuscula)
print(list(map(minuscula,cadena)))
