from functools import reduce
def sumar_reduce(x,y):
	"""Suma una secuencia de numeros con el metodo reduce()"""
	return x+y

lista=[1,2,5,6]
help(sumar_reduce)
print(reduce(sumar_reduce, lista))

