def funciona_a(funcion_b):
	def funcion_c():
		print("Antes de la ejecucion de la funcion a decorar")
		funcion_b()
		print("Despues de la ejecucion de la funcion a decorar")
	return funcion_c


@funciona_a
def saludar():
	print("hola mundo!!")

saludar()