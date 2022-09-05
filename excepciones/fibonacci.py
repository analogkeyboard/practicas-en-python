def fibonacci(n):
	if (n>=20) or (n<=0):
		print("ha ingresado un valor incorrecto")
		return

	salida=[]
	a,b=0,1

	for x in range(n):
		salida.append(b)
		a,b=b,a+b
	return salida

def main():
	e=input("ingresa n para calcular fibonacci(n): ")
	n=int(e)
	print(fibonacci(n))

main()