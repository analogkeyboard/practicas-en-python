class Coche(object):
	"""docstring for Coche"""
	def __init__(self,marca="porsche",modelo="911"):
		# super(Coche, self).__init__()
		self.marca = marca
		self.modelo = modelo

	def __repr__(self):
		return("{0}-{1}".format(self.marca,self.modelo))

	def __gt__(self,objeto):
		if int(self.modelo)>int(objeto.modelo):
			return True
		return False
		
# c=Coche()
# print(repr(c))

# arr=repr(c).split("-")
# d=Coche(arr[0],arr[1])
# print(d)
# print(arr)

modelo_911=Coche("nisan",911)
modelo_924=Coche("nisan",924)

if modelo_924>modelo_911:
	print("El {0} es un modelo superior".format(modelo_924.modelo))

