

filas=8
columnas=3
contador=1
m=[
[0]*filas for i in range(filas)
]



print(m)
print("\n"*2)

"""
# Rellena la matriz
for i in range(filas):
    for j in range(filas):
        # m[i][j]=contador
        print("Fila:["+str(i)+"]["+str(j)+"]",m[i][j])
    print()
"""

# Rellena la matriz
for i in range(filas):
    for j in range(filas):
        # m[i][j]=contador
        contador=contador+1
        
    
    
# Muestra la matriz    
for i in range(filas):
    for j in range(filas):
        
        # print(m[i][j],end="\t")
        print(str(i)+","+str(j),end="\t")
    print("\n")
print("-"*60)
print("\n")


# Muestra identidad   
for i in range(filas):
    for j in range(filas):
        if i==j:
            m[i][j]=1
        
        print(m[i][j],end="\t")
        # print(str(i)+","+str(j),end="\t"*2)
    print("\n"*2)
    
print("-"*60)
print("\n")

import unicodedata

# Muestra identidad   
for i in range(filas):
    for j in range(filas):
        if (i+j)%2==0:
            m[i][j]='░░'
        else:
            m[i][j]='██'
        
        if i==4 and j==4:
            m[i][j]='♝ '
            
        
        
        print(m[i][j],end="")
        # print(str(i)+","+str(j),end="\t"*2)
    print("")


print("-"*60)
print("\n")



