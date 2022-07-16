#funcion filter
def filtroNumPositivo(elem):
	return elem>0

lista=[1,-2,3,-6]

lista_respuesta=filter(filtroNumPositivo,lista)
print(lista_respuesta)

def FiltrodeCaracter(letra):
	return letra=='o'

cad="Coordinacion Cadena"

cad_respuesta=filter(FiltrodeCaracter,cad)
print(cad_respuesta)
