print("Posicion del alfil:")
renglon=int(input("Renglon: "))
columna=int(input("Columna: "))
print()
print(" i,j\t"*8)
for i in range(8):
    for j in range(8):
        print("("+str(i)+","+str(j)+")\t",end="")
    print("\n"*2)


    
