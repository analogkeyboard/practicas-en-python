class Padre(object):
	"""docstring for Padre"""
	def __init__(self):
		self.x=8
		print("Constructor clase padre")

	def metodo_padre(self):
		print("Ejecutando metodo de clase padre")

class Hija(Padre):
	def metodo_hija(self):
		print("Metodo hija")

hija=Hija()
hija.metodo_padre()
hija.metodo_hija()
print(hija.x)