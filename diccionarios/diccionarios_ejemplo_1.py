#diccionarios
#Los diccionarios
#Se les conoce como matriz asociativas
#No se utilizan indices , en vez de eso utilizamos
#las claves
diccionario={
	'c1':[1,2,3],
	'c2':True,
	'c3':False
}

#El diccionario imprime los valores de la clave 'c1'
print(diccionario['c1'])
print(diccionario['c2'])
print(diccionario['c3'])

#Los valores de cada clave se pueden modificar  excepto la clave 
diccionario['c1']=[4,5,6]
print(diccionario['c1'])

#Impresion del diccionario completo
print(diccionario)