def CuentaAtras_Generator(elemento):
	
	while elemento>0:
		yield elemento
		elemento=elemento-1

for elemento in CuentaAtras_Generator(10):
	print(elemento)




for elemento in CuentaAtras_Generator(10):
	print(elemento)