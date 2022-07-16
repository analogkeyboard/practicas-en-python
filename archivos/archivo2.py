print("Tablas de multiplicar usando archivos")
print("\n1.-Escribir una tabla de multiplicar")
print("2.-Leer una tabla de multiplicar")
print("3.-Salir o use CTRL+Z / CTRL+C")

entrada=None
try:
    while entrada!="":
        entrada=int(input("\nOpcion:"))
        print(entrada)

        if entrada==3:
            print("Programa Finalizado con Exito")
            break;

#captura el error end of file 
except EOFError as e:
    print("Programa Finalizado con CTRL+Z")

#captura el error keyboardInterrupt
except KeyboardInterrupt as e:
    print("Programa Finalizado con CTRL+C")

#siempre se ejecuta al finalizar el try/catch
finally:
    print("Finally Ejecutado")