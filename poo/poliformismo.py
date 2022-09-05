class Pajaro:

	def desplazar(self):
		print("volar")


class Serpiente:
	def desplazar(self):
		print("reptar")

def mover(animal):
	animal.desplazar()

p=Pajaro()
p.desplazar()

s=Serpiente()
s.desplazar()

mover(p)
mover(s)