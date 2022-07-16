def contadorVocales(texto):
  vocales="aeiou"
  cont=0
  for i in range(len(texto)):
    caracter=texto[i]
    print(caracter)

    if caracter in vocales:
      cont=cont+1
  
  return "numero de vocales: "+str(cont)


texto2="hola mundo"
print(contadorVocales(texto2))