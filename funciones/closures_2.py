def funcion_principal():
	x=7

	def funcion_anidada():
		print(x)

	return funcion_anidada()


res=funcion_principal()
print(res)
print(funcion_principal())
