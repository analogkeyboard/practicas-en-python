prueba_escritura=open("prueba 2.txt","a")
user=raw_input("Introduce tu Usuario: ")

prueba_escritura.write(user+"\n")



prueba_escritura=open("prueba 2.txt","r")
for i,linea in enumerate(prueba_escritura):
	linea=linea.rstrip("\n")
	print i+1,linea

prueba_escritura.close()