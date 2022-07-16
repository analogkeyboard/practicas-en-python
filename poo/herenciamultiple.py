#clases y objetos
class Humano:
	def __init__(self,edad,signo):
		self.edad=edad
		self.signo=signo
		print "soy un nuevo objeto"

	def hablar(self,mensaje):
		print mensaje

class Ingeniero(Humano):
	#si una clase  tiene su propio metodo __init__
	#tendra prioridad a la hora de instanciar un objeto de la clase
	def __init__(self):
		print "Hola soy un ingeniero"

	def programar(self,lenguaje):
		print "programare en",lenguaje

class Derecho(Humano):
	def __init__(self,escuela):
		print "soy un licenciado"

	def estudiar(self,der):
		print "estudiare el caso",der

class estudioso(Derecho,Ingeniero):
	#si no existe un metodo se le colo la palabra
	#reservada pass
	pass		
	
tania=estudioso("unam")
tania.hablar("soy herencia multiple")
tania.programar('python')
tania.estudiar("corrupcion")

