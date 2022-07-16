import pprint
i=1
m=[
[0]*8,
[0]*8,
[0]*8,
[0]*8,
[0]*8,
[0]*8,
[0]*8,
[0]*8
]

n=['\n']

print(m)

for x in range(8):
    for y in range(8):
        m[x][y]=i
        i=i+1
        # print("\n")


print(m)
print()
        
for x in range(8):
    for y in range(8):
        print(m[x][y],"\t",end="")
    print("\n")    
   
        

# print(m)
# m[0][1]=1
    
# pprint(m[2][1])