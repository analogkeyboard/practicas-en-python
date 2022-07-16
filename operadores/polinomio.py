
a=5
b=4
c=3
x=2

#potencia multiplicando la variable por si misma
resultado=a*(x*x*x)+b*(x*x)-c*x+3
print("ax^3+bx^2-cx+3")
print("Resultado:",resultado)

#potencia usando la funcion math.pow
import math
resultado2=a*(math.pow(x,3))+b*(math.pow(x,2))-c*x+3
print()
print("ax^3+bx^2-cx+3")
print("Resultado2 :",resultado2)