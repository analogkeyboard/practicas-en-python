potencia_2=[]

for numero in range(0,11):
	potencia_2.append(numero**2)

print(potencia_2)

pares=[]

for numero in potencia_2:
	if numero%2==0:
		pares.append(numero)
print(pares)