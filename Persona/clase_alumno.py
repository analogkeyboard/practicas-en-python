from clase_persona import *

class AlumnoFIUBA():
	"""docstring for AlumnoFIUBA"""
	def __init__(self,identificacion,nombre,apellido,padron):
		# super(AlumnoFIUBA, self).__init__()
		Persona.__init__(self,identificacion, nombre, apellido)
		self.padron = padron
		
	def __str__(self):
		return "%d: %s, %s" % (self.padron,self.nombre,self.apellido)

