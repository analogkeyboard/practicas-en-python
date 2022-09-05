class Punto(object):
	def __init__(self,x=0,y=0):

		if es_numero(x) and es_numero(y):

			self.x = x
			self.y = y

		else:
			raise TypeError("X e Y deben ser valores numericos")

	# def distancia(self,otro):
	# 	dx=self.x-otro.x
	# 	dy=self.y-otro.y
	# 	print("dx:",dx)
	# 	print("dy:",dy)
	# 	print("dx**0.5:",dx*dx)
	# 	print("dy**0.5:",dy*dy)
	# 	print(25**0.5)
	# 	return (dx*dx + dy*dy)**0.5

	def distancia(self,otro):
		r=self.restar(otro)
		return r.norma()

	def restar(self,otro):
		return Punto(self.x-otro.x,self.y-otro.y)


	def norma(self,otro):
		return (self.x*self.x + self.y*self.y)**0.5
		
	def __str__(self):
		return "("+str(self.x)+", "+str(self.y)+")"


	def __add__(self,otro):
		return Punto(self.x+otro.x,self.y+otro.y)

	def __sub__(self,otro):
		return Punto(self.x-otro.x,self.y-otro.y)

	def __eq__(self, otro):

		return self.x == otro.x and self.y == otro.y
		
	def __ne__(self, otro):

		return not self == otro

def es_numero(valor):
	return isinstance(valor, (int,float,complex))
p=Punto(3,4)
q=Punto(2,5)
# print("Objeto:",p)
# print("Punto x:",p.x)
# print("Punto y:",p.y)
# print("Distancia:",p.distancia(q))

# print(p-q)
# print(p+q)

