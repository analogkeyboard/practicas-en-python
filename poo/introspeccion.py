class Introspeccion:
	def __init__(self,val):
		self.x=val

	def primero(self):
		print("primero")

	def segundo(self):
		print("segundo")


class Hijo(Introspeccion):
	def tercero(self):
		print("tercero")

i=Introspeccion("Valor")

print(dir(i))
print(isinstance(i, Introspeccion))
print(hasattr(i, 'x'))


h=Hijo("v")
print(dir(h))
print(hasattr(h, 'x'))
print(isinstance(h, Introspeccion))

print(type(i))
print(type(h))

cad="cadena"
print(callable(cad))

def fun():
	pass


print(callable(fun))
print(callable(i))

