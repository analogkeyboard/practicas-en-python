class Persona(object):
	"""docstring for Persona"""
	def __init__(self,identificacion,nombre,apellido):
		# super(Persona, self).__init__()
		self.identificacion = identificacion
		self.nombre = nombre
		self.apellido = apellido

	def __str__(self):
		return "%s: %s, %s" % (str(self.identificacion),self.nombre,self.apellido)

# class AlumnoFIUBA(Persona):
# 	"""docstring for AlumnoFIUBA"""
# 	def __init__(self,identificacion,nombre,apellido,padron):
# 		# super(AlumnoFIUBA, self).__init__()
# 		Persona.__init__(self,identificacion, nombre, apellido)
# 		self.padron = padron
		
# 	def __str__(self):
# 		return "%d: %s, %s" % (self.padron,self.nombre,self.apellido)

