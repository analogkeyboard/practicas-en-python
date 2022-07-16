#clases y objetos
class Humano:
	def __init__(self,edad,signo):
		self.edad=edad
		self.signo=signo
		print("soy un nuevo objeto")


	def hablar(self,mensaje):
		print(mensaje)

class Ingeniero(Humano):
	def __init__(self):
		print("Hola soy un ingeniero")

	def programar(self,lenguaje):
		print("programare en",lenguaje)

class Derecho(Humano):
	def estudiar(self,der):
		print("estudiare el caso",der		)
	
tania=Ingeniero();
#tania = Ingeniero(27,'geminis')
#print('edad',tania.edad,'signo',tania.signo)
tania.hablar("holis")
tania.programar('python\n')

pedro = Derecho(29,'cancer')
print('edad',pedro.edad,'signo',pedro.signo)
pedro.hablar("hola")
pedro.estudiar('leyes')
