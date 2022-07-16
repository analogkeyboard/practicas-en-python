entrada_usuario=abs(int(input("introduce un numero: ")))
print("\nnumero introducido: ",entrada_usuario)

contador=0
while entrada_usuario>0:
  print("debug: ",contador,":",entrada_usuario)
  entrada_usuario=entrada_usuario//10
  contador=contador+1

print("\nNumero de digitos: ",contador)
