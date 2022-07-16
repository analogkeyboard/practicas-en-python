#encapsulasion
class Prueba():
	
	def __init__(self):
		
		self.__private = "Soy privado"
		self.publico="Soy publico"

	def __metodoPrivado(self):
		return "Soy un metodo privado"

	def metodoPublico(self):
		print("Soy un metodo publico")

	def getPrivado(self):
		return self.__private

	def setPrivado(self,valor):
		self.__private=self.__metodoPrivado()

obj=Prueba()

#print obj.publico
#print obj.__private
print(obj.getPrivado())
obj.metodoPublico()
obj.setPrivado("Soy un valor privado")
#obj.__metodoPrivado()
print(obj.getPrivado())