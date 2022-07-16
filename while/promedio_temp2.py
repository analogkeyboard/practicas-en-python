#lista=[15,54,56,89]
l=[]
suma=0
promedio=0
cont=1
n=None
while cont<5:
  print("introduce un valor",cont,":")
  user=int(input())
  l.append(user)
  suma+=l[cont-1]
  promedio=suma/4
  cont+=1
  

print(n)
print("lista:",l)
print("suma:",suma)
print("promedio",promedio)
