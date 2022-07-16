import random
alfabeto="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros="0123456789"
total_licencias=20

print("\n\nGenerador de matriculas de autos")
for i in range(total_licencias):
  num1=random.choice(numeros)
  num2=random.choice(numeros)
  num3=random.choice(numeros)
  num4=random.choice(numeros)
  
  letra1=random.choice(alfabeto)
  letra2=random.choice(alfabeto)
  letra3=random.choice(alfabeto)
  print("Matricula {}:\t{}{}{}{}-{}{}{}".format(i+1,num1,num2,num3,num4,letra1,letra2,letra3))