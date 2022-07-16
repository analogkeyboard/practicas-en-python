filas=8
columnas=3
contador=1
m=[
[0]*filas for i in range(filas)
]

for i in range(filas):
    for j in range(filas):
        
        # print(m[i][j],end="\t")
        print(str(i)+","+str(j),end="\t")
    print("\n")
print("-"*60)
print("\n")

pos_i=4
pos_j=4
# Muestra identidad   if i==4 and j==4 and 
for i in range(filas):
    for j in range(filas):
        
        
        if (i+j)%2==0:
            m[i][j]='N'
        else:
            m[i][j]='B'
        
        m[pos_i][pos_j]='*'
        
        if (i+j)==pos_i and (i+j)==pos_j and (i-j)%2==0 or (i-j)==0 and i!=j:
            m[i][j]='*'
            
        print(m[i][j],end="\t")
        # print(str(i)+","+str(j),end="\t"*2)
    print("\n")

print("-"*60)
print("\n")




print("-"*60)
print("\n")