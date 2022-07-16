
texto=None
if texto!="":
    #texto=input("Introduce un texto o presiona ENTER para salir: ")
    try:
        while texto!="":
                texto=input("Introduce un texto o presiona ENTER para salir: ")
                for x in texto:
                    print("El codigo ascii de "+x+" es "+str(ord(x)))
    except EOFError:
            print("Programa interrumpido: CTRL + Z")
    
    finally:
        print("Fin del programa")   

