lista=['hola','mundo',"chanchito","feliz","dragones"]
print("lista:",lista)
dato =input("Dame un dato: ")


if lista.count(dato) > 0 :
    print("el dato existe:",dato)
else:
    print("el dato no existe",dato)