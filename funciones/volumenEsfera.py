#escribit una funcion que devuelva el volumen de una esfera por su radio
#formula: 4/3 * pi* r **3

from math import pi,pow
def calculaVolumen(r):
    volumen1 = (4/3)*pi*pow(r,3)
    print(pi,pow(r,3)) 
    print(r**3) 
    volumen2 = (4/3)*3.14*(r**3) 
    print(volumen1)
    print(volumen2)

calculaVolumen(6)