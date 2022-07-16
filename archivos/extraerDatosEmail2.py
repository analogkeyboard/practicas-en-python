correo="tania@gmail.com"
a=correo.partition("@")
#print("{}".format(a[0]))
print("usuario: "+a[0])
print("dominio: "+a[1]+a[2])