class Vehiculo(object):
	"""docstring for Vehiculo"""
	num_ruedas=2
	def __init__(self, marca,modelo):
		self.marca=marca
		self.modelo=modelo

	def acelerar(self):
		pass

	def frenar(self):
		pass

class Moto(Vehiculo):
	pass

class Coche(Vehiculo):
	pass


coche=Coche("porsche", "944")
coche.num_ruedas=4
print("Numero de ruedas de coche:",coche.num_ruedas)

moto=Moto("Honda", "Goldwin")	
print("Numero de ruedas de moto:",moto.num_ruedas)