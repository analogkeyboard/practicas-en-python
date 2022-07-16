lista=[1,2,3,-1,4,5]
cadena=['a','b','c','d','e']

lista_2=[num for num in lista if num>0]

lista_3=(c*l for c in cadena
				for l in lista
					if l > 0 )

print(lista)
print(lista_2)
print(lista_3)

def factorial(n):
	i=1
	while n>1:
		i=n*i
		yield i
		n -= 1

print(factorial(5))

for letra in lista_3:
	print(letra)

for num in factorial(5):
	print(num)