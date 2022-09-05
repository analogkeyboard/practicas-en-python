def nombre_decorador(nombre):

	def decorador(funcion):

		def wrapper(*args,**kwargs):

			print("Nombre:",nombre)

			return funcion(*args,**kwargs)

		return wrapper

	return decorador

@nombre_decorador("el decorador de Tania")
def suma(a,b):
	return a+b


print(suma(4,5))