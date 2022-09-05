class Dog:
	"""docstring for Dog"""
	especie="Canis familiaris"
	def __init__(self, nombre,edad):
		# super(Dog, self).__init__()
		self.nombre = nombre
		self.edad = edad

	# def descripcion(self):
	# 	return f"{self.nombre} tiene {self.edad} años"

	def __str__(self):
		return f"{self.nombre} tiene {self.edad} años"
		
	def hablar(self,sonido):
		return f"{self.nombre} dice {sonido}"
		