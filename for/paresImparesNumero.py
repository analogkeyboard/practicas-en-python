n=input("Dame un numero: ")
par=0
impar=0

for i in n:
  if int(i)%2==1:
    impar=impar+1
  else:
    par=par+1
  
print("numeros pares: ",par)
print("numeros impares: ",impar)