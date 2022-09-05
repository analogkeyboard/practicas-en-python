def saludar():
	print("hola soy una funcion")

def super_funcion(funcion):
	funcion()

funcion=saludar

funcion()

super_funcion(funcion)