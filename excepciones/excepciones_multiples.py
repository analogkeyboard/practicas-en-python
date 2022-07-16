try:
    n=int(input("dame un numero: "))
    print(5/n)
except Exception as e:
    print(e)
    print(type(e))

    print("\n\n\n\n")

def valorNulo(x=None):
    try:
        if x is None:
            raise ValueError("No se permite un valor nulo")
    except ValueError:
            print("no se permite valor nulo (excepsion)")
valorNulo("algo")
valorNulo()