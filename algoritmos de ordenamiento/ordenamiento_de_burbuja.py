import os
l=[91, 52, 5, 85,78,45, 70, 23, 99, 56, 22, 2]
# print(len(l),"\n\n")
print("Lista Sin Ordenar: ",l,"\n\n")
i=0
j=0
largo=len(l)
while i<=largo:
	for j in range(largo-1):
		print("["+str(i+1)+"] ",l,"\n")
		# print("iteracion[",i,"]=",l)
		if l[j]>l[j+1]:
			
			temp=l[j]
			l[j]=l[j+1]
			l[j+1]=temp

		# print(temp,"\t",l[j],"\t",l[j+1])
		# print("\n"*2)
		os.system('pause')
	i=i+1
print("Lista Ordenada: ",l)