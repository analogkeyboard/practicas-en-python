class Decorador(object):
	"""docstring for Decorador"""
	def __init__(self, f):
		self.f = f

	def __call__(self,*args):
		print("Inicio:",self.f.__name__)
		self.f(*args)
		print("Fin:",self.f.__name__)

@Decorador
def funcion(p1,p2,p3):
	print("Soy una funcion con los argumentos",p1,",",p2," y ",p3)

funcion("a","b","c")