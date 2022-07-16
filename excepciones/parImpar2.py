#programa que muestra si el numero es par o impar
#forma 1

#n=int(input("introduce un numero: "))
n=0
while n!=-1:
    try:
        n=int(input("introduce un numero: "))
    except ValueError:
        print("no es un entero!")
        continue
    else:
        if n%2==0:
            print("El numero ",n," es par")
        else:
            print("El numero ",n," es impar")

print("programa finalizado")