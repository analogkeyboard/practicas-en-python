#forma 1
lista=[45,650,54,728,61]
lista_final=[]
for i in lista:
 if i%2==0:
  lista_final.append(i//10)
  print(i)

print(lista_final)