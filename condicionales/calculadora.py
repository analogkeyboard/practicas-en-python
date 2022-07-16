#calculadora de suma

dato1=input("numero 1: ")



try:
    dato1=int(dato1)
except :
    dato1="string"

if dato1=="string":
    print("los valores deben ser numericos")
    exit()
dato2=input("numero 2: ")
try:
    dato2=int(dato2)
except :
    dato2="string"

if dato2=="string":
    print("los valores deben ser numericos")
    exit()

operacion=input("operacion: ")

if operacion=='+':
    print(dato1+dato2)

elif operacion=='-':
    print(dato1-dato2)

elif operacion=='*':
    print(dato1*dato2)

elif operacion=='/':
    print(dato1/dato2)
else:
    suma=dato1+dato2

    