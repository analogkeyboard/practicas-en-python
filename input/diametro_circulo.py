import math 
#radio=10
numero_pi=math.pi

radio=int(input("Radio: "))
diametro=2*radio
circunferencia=2*numero_pi*radio
area=numero_pi*(math.pow(radio,2))

print("\nDatos del circulo")
print("Radio:",radio)
print("PI:",numero_pi)
print()
print("Diametro:",diametro)
print("Circunferencia:",circunferencia)
print("Area:",area)
