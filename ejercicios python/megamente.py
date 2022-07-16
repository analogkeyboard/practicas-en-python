import random as r
digitos=('1','2','3','4','5','6','7','8','9')
codigo=""

for x in range(4):
    candidato=r.choice(digitos)
    codigo=codigo+candidato
    print("["+str(x)+"]="+codigo)
print(codigo)

acierto=0
intentos=0
print("adivina el numero")
propuesta=input("Numero: ")

while propuesta!=codigo:
    intentos=intentos+1
    acierto=0
    concidencias=0
    for i in range(4):
        if propuesta[i]==codigo[i]:
            acierto=acierto+1
        elif propuesta[i] in codigo:
            concidencias=concidencias+1
    print("tu propuesta (",propuesta,") tiene ",acierto," aciertos y ",concidencias," coincidencias")
    propuesta=input("Numero: ")
print("felicidades , adivinaste el codigo en ",intentos,"intentos")
        
            