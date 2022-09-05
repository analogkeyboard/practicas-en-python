class EjemploGetterProperty(object):
	def __init__(self, var):
		self.__a = var
	@property
	def a(self):
		return self.__a

	@a.setter
	def a(self,var):
		if var > 0 and var%2==0:
			self.__a=var
		else:
			self.__a=2

e =EjemploGetterProperty(10)
e.a=12
print(e.a)
