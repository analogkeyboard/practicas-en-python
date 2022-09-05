from math import pi

class Circle():
	"""docstring for Circle"""
	
	@property
	def radio(self):
		return self.__radio

	@radio.setter
	def radio(self,radio):
		self.radio=radio

c=Circle()
c.radio=23
print(c.radio)
	