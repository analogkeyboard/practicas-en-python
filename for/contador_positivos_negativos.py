print("Introduce 5 numeros")
try:
    positivos=0
    negativos=0
    nulos=0
    for x in range(5):
        n=int(input("Numero "+str(x+1)+"= "))
        
        if n>0:
            positivos=positivos+1
        elif n<0:
            negativos=negativos+1
        else:
            nulos=nulos+1
except ValueError:
    print("El valor debe ser un numero")

finally:
    print("\nPositivos:",positivos)
    print("Negativos:",negativos)
    print("Nulos:",nulos)