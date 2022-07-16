import random as r

#genera 10 numeros aleatorios entre 0 y 50
lista_0y50=[]
for item in range(10):
    ran_num=r.randint(0,50)
    lista_0y50.append(ran_num)
print("\nnumeros entre 0 y 50\n",lista_0y50)


#genera 20 numeros aleatorios entre 0 y 100
lista_0y100=[]
for item in range(20):
    ran_num=r.randrange(0,100,2)
    lista_0y100.append(ran_num)
print("\nnumeros entre 0 y 100\n",lista_0y100)

#genera 10 numeros multiplos de 5 entre 0 y 100

print("\nnumeros multiplos de 5")
for item in range(10):
    mul_5=r.randint(0,50)*5
    print(mul_5,end=" ")
 
