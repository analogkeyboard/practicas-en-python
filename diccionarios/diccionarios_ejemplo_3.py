diccionario={
'fruta 1':'manzana',
'fruta 2':'pera',
'fruta 3':'naranja',
}

print(diccionario)
dic=str(diccionario)
print(dic.split(':'))
with open("test.txt","w") as fichero:
	for k,v in diccionario.items():

		# print(k,v)

		fichero.write(str(k)+":"+str(v)+"\n")