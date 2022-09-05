class Nodo(object):
	"""docstring for Nodo"""
	def __init__(self, dato=None,prox=None):
		self.dato = dato
		self.prox = prox
	
	def __str__(self):
		return str(self.dato)

v4=Nodo()
v3=Nodo("Bananas",v4)
v2=Nodo("Peras",v3)
v1=Nodo("Manzanas",v2)

# print(v1)
# print(v2)
# print(v3)

def verLista(nodo):
	while nodo:
		print(nodo)
		nodo=nodo.prox

lista=v2
verLista(lista.prox)

