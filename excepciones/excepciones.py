
while True:
    

    try:
        n= float(input("introduce un numerio: "))
        m=4
        print(n,m,n/m)
        
    except:
        print("ha ocurrido un error, ingrese un numero")

    else:
        break

    finally:
        print("ejecucion terminada")
