#formato
#id:type:country:name:password:current_time
archivo=open("data.txt","r")
usuario=open("usuario.txt","w")
password=open("password.txt","w")

for line in archivo:
  partes=line.split(":")
  #print(partes)
  nombre=partes[3]
  contrasena=partes[4]
  #print("{}\t{}".format(nombre,contrasena))
  usuario.write(nombre+"\n")
  password.write(contrasena+"\n")

archivo.close()
usuario.close()
password.close()

