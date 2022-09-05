#usando map sin lambda
def cuadrado(n):
	return n*n

lista1=[1,2,3,4,5]
numero_cuadrado=list(map(cuadrado,lista1))
print(numero_cuadrado)

#usando map con lambda
lista2=[1,2,3,4,5]
numero_cuadrado2=list(map(lambda x: x * x, lista2))
print(numero_cuadrado2)