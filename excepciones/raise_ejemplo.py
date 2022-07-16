def dividir(dividendo,divisor):
    try:
        resultado= dividendo/divisor
        return resultado
    except ZeroDivisionError:
        raise ZeroDivisionError("El divisor no puede ser cero")

print(dividir(1,0))