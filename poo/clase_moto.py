class Moto:
	numero_ruedas=2

	def __init__(self,marca,modelo,color):
		self.marca=marca
		self.modelo=modelo
		self.color=color

		print("Marca: "+self.marca)
		print("Modelo: "+self.modelo)
		print("Color: "+self.color)
		print()

	def get_marca(self):
		marca="nueva marca"
		print(self.marca)

	def acelerar(self,km):
		print("acelerando {0} km".format(km))

moto1=Moto("toyota","1200","rojo")
moto2=Moto("honda","1300","azul")

print("marca de la moto 1:",moto1.marca)
print("color de la moto 1:",moto1.color)
print("color de la moto 2:",moto2.color)

print(moto1.get_marca())
print(moto1.acelerar(500))
print(Moto.numero_ruedas)
print(moto2.numero_ruedas)