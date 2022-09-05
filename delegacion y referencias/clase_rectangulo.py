from punto import Punto

class Rectangulo(object):
	"""docstring for Rectangulo"""
	def __init__(self, base,altura,origen):
		# super(Rectangulo, self).__init__()
		self.base = base
		self.altura = altura
		self.origen = origen

	def trasladar(self,dx=0,dy=0):
		self.origen=self.origen+Punto(dx,dy)

	def area(self):
		return self.base*self.altura

	def __str__(self):
		return "Base: %s, Altura: %s, Esquina inf. izq.: %s " % (self.base, self.altura, self.origen)

r=Rectangulo(2, 3, Punto(1,2))
print(r)
print(r.area())