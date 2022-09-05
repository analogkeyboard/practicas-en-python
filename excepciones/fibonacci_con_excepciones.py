def fibonacciConExcepciones(n):
	try:
		assert(n>0)
		assert(n<20)
	except AssertionError:
		raise ValueError

	a=0
	b=1
	salida=[]

	for x in range(n):
		salida.append(b)
		a,b=b,a+b

	return salida

def mainConExcepciones():
	try:
		e=input("ingrese n para calcular fibonacci(n): ")
		n=int(e)
		print(fibonacciConExcepciones(n))

	except ValueError:
		print("ha ingresado un valor incorrecto")

mainConExcepciones()