import math
"""
n:0 #numero
aprox=0 #aproximacion a la raiz cuadrada
antaprox=0 #anterior aproximacion a la raiz cuadrada
epsilon=0 #coeficiente de error
"""
try:
    n=-1
    while n<0:
        n=float(input("Numero: "))
    aprox=-1
    while aprox<=0:
        aprox=float(input("Raiz cuadrado aproximada: "))
    epsilon=-1
    while epsilon<=0:
        epsilon=float(input("Coeficiente de error: "))


    antaprox=0
    while (abs(aprox-antaprox)>=epsilon ):
        antaprox=aprox
        aprox=(n/antaprox+antaprox)/2

    print("La raiz cuadrada de ",format()," es ",aprox)
except TypeError:
    print("Error de tipo")
except ZeroDivisionError:
    print("Division entre cero")
