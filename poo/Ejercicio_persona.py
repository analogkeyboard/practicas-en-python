class Persona(object):

	def __init__(self,nombre,edad):
		self.__nombre=nombre
		self.__edad=edad

	"""docstring for Persona"""
	def set_nombre(self,nombre):
		self.__nombre=nombre

	def set_edad(self,edad):
		self.__edad=edad

	def get_nombre(self):
		return self.__nombre

	def get_edad(self):
		return self.__edad

	def print_persona(self):
		return "Mi nombre es es{0} y mi edad es{1}".format(self.__nombre,self.__edad)

	
persona=Persona("joan", "15")
print("nombre:",persona.get_nombre())
print("edad:",persona.get_edad())
print(persona.print_persona())
persona.set_nombre("ola")
print(persona.get_nombre())
	
	