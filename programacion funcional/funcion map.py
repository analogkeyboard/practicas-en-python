def operador(n,m):
	if n==None or m==None:
		return 
	return n+m

lista=[1,2,3,4]
tupla=(9,8,7)

resultado= map(operador,lista,tupla)
print(lista)
print(tupla)
print(resultado)

cad1='Hola'
cad2='Mundo'
cad3=map(operador,cad1,cad2)
print(cad3)
