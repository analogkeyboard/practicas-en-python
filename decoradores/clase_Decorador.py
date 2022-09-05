class Decorador(object):
	"""docstring for Decorador"""
	def __init__(self, f):
		self.f = f

	def __call__(self):
		print("Inicio:",self.f.__name__)
		self.f()
		print("Fin:",self.f.__name__)

@Decorador
def funcion():
	print("Soy una funcion")

funcion()