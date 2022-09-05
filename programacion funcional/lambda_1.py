def operar(v1,v2,fn):
	return fn(v1,v2)

resultado1=operar(10, 3, lambda x1,x2:x1+x2)
print(resultado1)

resultado2=operar(10, 3, lambda x1,x2:x1-x2)
print(resultado2)

resultado3=operar(10, 3, lambda x1,x2:x1*x2)
print(resultado3)

resultado4=operar(10, 3, lambda x1,x2:x1/x2)
print(resultado4)

resultado5=operar(10, 3, lambda x1,x2:x1//x2)
print(resultado5)