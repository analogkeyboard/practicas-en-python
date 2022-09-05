def contenedora(a):
	def anidada(b):
		return a+b

	return anidada

fun=contenedora(9)

print(fun(12))

otra=contenedora(1)
print(otra(12))