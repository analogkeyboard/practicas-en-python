#programa que suma los numeros de 0 a n numeros

tam=int(input("cantidad de numeros: "))
suma=0
for i in range(tam):
    suma+=i
    print("debug: ",suma,",",i)


print("suma: ",suma)