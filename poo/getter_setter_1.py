class EjemploGetterSsetter:
	"""docstring for EjemploGS"""
	def __init__(self,a):
		self.__a=a

	def get_a(self):
		return self.__a

	def set_a(self,a):
		self.__a=a

e=EjemploGetterSsetter(10)
print(e.get_a())
print(e.__a)
e.__a=11
print(e.get_a())
e.set_a(11)
print(e.get_a())