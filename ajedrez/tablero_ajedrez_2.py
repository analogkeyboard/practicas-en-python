print()
print(" i,j\t"*8)
k=8
for i in range(8):
    for j in range(65,73):
        print("("+str(k)+","+chr(j)+")\t",end="")
    k=k-1
    print("\n"*2)   