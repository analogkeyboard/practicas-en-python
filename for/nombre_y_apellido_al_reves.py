#ingresar un nombre y apellido e imprimirl al reves
print("ingresar un nombre y apellido e imprimirl al reves\n")
nombre="tania"
apellido="feliz"
concatenacion=nombre+" "+apellido
print("Cadena original: "+concatenacion)
print("Cadena al reves: "+concatenacion[::-1])

print()
for i in concatenacion[::-1]:
    print(i,end='')
