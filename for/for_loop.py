
usuarios=['juan','karen','saku']
print("lista:",usuarios)

i=0
for elementos in usuarios:
    i+=1
    print("elemento["+str(i)+"]",elementos)

cadena="palabra"
print("cadena separada")
for c in cadena:
    print(c)


print("cadena separada en horizontal")
for c in cadena:
    print(c,end="\t")

print("\nimpresion de numeros con range\n")
for item in range(10):
    print(item)