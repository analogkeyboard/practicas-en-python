lista=[1,2,3,-1,0-34-56,4,5]
cadena=['a','b','c','d','e']

lista_2=[num for num in lista if num>0]

lista_3=[c*l for c in cadena
				for l in lista
					if l > 0 ]

print("cadena:",cadena)
print("Lista 1:",lista)
print()
print("Lista 2:",lista_2)
print()
print("Lista 3:",lista_3)