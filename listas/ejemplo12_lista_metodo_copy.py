print("\nMetodo copy")
lista_a=[1,2,3]
lista_b=lista_a.copy()

print("Lista original: ",lista_a)
print("Lista copia: ",lista_b)


lista_a.append(5)
print("\nLista original con elemento 5 agregado: ",lista_a)

lista_b.append(0)
print("Lista copia con elemento 0 agregado: ",lista_b)


print("\nLista original actualizada: ",lista_a)
print("Lista copia actualizada: ",lista_b)

