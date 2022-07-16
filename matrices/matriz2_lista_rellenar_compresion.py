print("Matrices en python con listas")

matriz=[0,5,3]
matriz2=[1,2,3]

# print("Matriz original vacia:",matriz)

# matriz=[[None]*3]
# print("Matriz :",matriz)

matriz=[
i for i in matriz 
for j in matriz2 
if i==j
]
print("Matriz :",matriz)