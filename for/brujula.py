filas=3
# v=[[1,4,6],[6,7,4],[4,5,6]]
print("\n"*3)
v=[[0]*filas for _ in range(filas)]

for i in range(3):
    for j in range(3):
        # print("\t"*2,v[i][j],end="\t")
        
        print("\t"*2,str(i)+","+str(j),end="\t")
    print("\n"*3)

print("Matriz Sin valores:",v)
# v[1][1]='*'
print("Matriz Con valor central:",v[1][1])

pos_i=1
pos_j=1
for i in range(3):
    for j in range(3):
        if i==1 and j==1:
            v[i][j]='*'
        
        if (j-1<pos_j ) and (i==pos_i ) and( i!=j):
            v[i][j]='O'
        
        elif (j+1>pos_j ) and (i==pos_i ) and( i!=j):
            v[i][j]='E'
        
        elif (i-1<pos_i ) and (j==pos_j ) and( i!=j):
            v[i][j]='N'
            
        elif (i+1>pos_i ) and (j==pos_j ) and( i!=j):
            v[i][j]='S'
            
        elif i==0 and j==0:
            v[i][j]='NO'
            
        elif (i+1>pos_i ) and (j==0 ):
            v[i][j]='SO'
        # print("\t"*2,v[i][j],end="\t")
        
        elif (i-1<pos_i ) and (j==2 ):
            v[i][j]='NE'
        # print("\t"*2,v[i][j],end="\t")
        
        elif (i==2 ) and (j==2):
            v[i][j]='SE'
        print("\t"*2,v[i][j],end="\t")
        # print("\t"*2,str(i)+","+str(j),end="\t")
    print("\n"*3)




# v=[i for i in range(filas) for j in range(3)]
# print(v)