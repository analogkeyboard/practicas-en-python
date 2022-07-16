def prueba(f):
	return f()

def porEnviar():
	return 2+2

print("2+2:",prueba(porEnviar))
print("")

#funciona en una variable
def seleccion(operacion):
	def suma(n,m):
		return n+m

	def multiplicacion(n,m):
		return n*m

	if operacion=='suma':
		return suma
	if operacion=='multiplicacion':
		return multiplicacion

fGuardada=seleccion('multiplicacion')
print('multiplicacion:',fGuardada(5,5))

fGuardada=seleccion('suma')
print('suma:',fGuardada(5,5))