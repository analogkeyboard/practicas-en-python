class Test:
	def __init__(self):
		self.x=8

	@classmethod
	def metodo_clase(cls,param1):
		print("parametro: {0}".format(param1))

	@staticmethod
	def metodo_estatico(valor):
		print("valor: {0}".format(valor))
		

t=Test()
Test.metodo_clase(1)
t.metodo_clase(10)
print(t.x)
t.metodo_estatico(15)