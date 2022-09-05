def medir_tiempo(funcion):
	def wrapper(*args,**kwargs):
		import time

		start=time.time()
		result=funcion(*args,**kwargs)
		total=time.time()-start

		print("inicio-",start,"segundos")
		print("total-",total,"segundos")
		print("resultado-",result,"segundos")

		return result

	return wrapper

@medir_tiempo
def suma(a,b):
	import time
	time.sleep(1)
	return a+b


print(suma(1,7))

