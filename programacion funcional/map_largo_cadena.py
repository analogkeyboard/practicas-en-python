def largo_cadena(cadena):
	return len(cadena)

cadena=["el" ,"largo" ,"de " ,"la cadena"]
cadena2="el largo de la cadena"
print(cadena2.split())

print(list(map(largo_cadena,cadena)))
