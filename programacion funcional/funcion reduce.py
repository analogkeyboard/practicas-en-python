s=('h','o','l','a',' ','m','u','n','d','o')

def concatenar(a,b):
	return a+b	

sr=reduce(concatenar,s)

print(type(sr))
print(sr)


suma=(1,2,3,4,5,6,7,8,9,10)

def suma_de_cifra(a,b):
	return a+b

resultado=reduce(suma_de_cifra,suma)

print(type(resultado))
print(resultado)