diccionario={
	'item1':[1,2,'tres'],
	'item2':'dos',
	'item3':'Hola Mundo'
}

#imprime el diccionario
#en forma inversa por default
print("diccionario",diccionario)

print("claves",diccionario.keys())
print("valores",diccionario.values())

print("Elemento eliminado",diccionario.pop('item4','\nError'))
print(diccionario)

del diccionario['item2']

print(diccionario)

#diccionario.clear()

print(diccionario)

diccionario['item4']='valor 4'

dic2 = diccionario.copy()

print("Copia de diccionario:",dic2)


