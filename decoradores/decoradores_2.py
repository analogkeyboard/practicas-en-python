def funciona_a(funcion_b):
	def funcion_c(*args,**kwargs):
		print("Antes de la ejecucion de la funcion a decorar")
		result=funcion_b(*args,**kwargs)
		print("Despues de la ejecucion de la funcion a decorar")
		return result


	return funcion_c


@funciona_a
def suma(a,b):
	return a+b

print(suma(3,4))