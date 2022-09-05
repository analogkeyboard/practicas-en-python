def es_cadena_no_vacia(cadena):
	return cadena!=''

def es_numero(valor):
	return isinstance(valor, (int,float,complex))


class Hotel(object):
	"""docstring for Hotel"""
	def __init__(self, nombre='*',ubicacion='*',puntaje=0,precio=float("inf")):
	# def __init__(self, nombre='*'):

		if es_cadena_no_vacia(nombre):
			self.nombre=nombre
		else:
			raise TypeError("El nombre debe ser una cadena no vacia")
		
		if es_cadena_no_vacia(ubicacion):
			self.ubicacion=ubicacion
		else:
			raise TypeError("La ubicacion debe ser una cadena no vacia")

		if es_numero(puntaje):
			self.puntaje=puntaje
		else:
			raise TypeError("El puntaje debe ser un numero")

		if es_numero(precio):
			if precio!=0:
				self.precio=precio
			else:
				self.precio=float("inf")

		else:
			raise TypeError("El precio debe ser un numero")


	def ratio(self):
			return ((self.puntaje**2)*10.)/self.precio

	def __cmp__(self,otro):
			diferencia=self.ratio()-otro.ratio()
			if diferencia<0:
				return -1
			elif diferencia>0:
				return 1
			else:
				return 0


	def __str__(self):
 		return self.nombre + " de "+ self.ubicacion+ \
 			" - Puntaje: " + str(self.puntaje) + " - Precio: "+ \
 			str(self.precio)+ " pesos."



h1=Hotel("Hotel 1* normal", "MDQ", 1, 10)
h2=Hotel("Hotel 2* normal", "MDQ", 2, 40)
h3=Hotel("Hotel 3* carisimo", "MDQ", 3, 130)
h4=Hotel("Hotel vale la pena" ,"MDQ", 4, 130)
lista=[h1,h2,h3,h4]

lista.sort()

for hotel in lista:
	print(hotel)
	

# print(hotel2<hotel1)
print(h1.ratio())
print(h2.ratio())
print(h3.ratio())
print(h4.ratio())

		