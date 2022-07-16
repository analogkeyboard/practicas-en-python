email_test="tania@yahoo.com"
#email=input("Introduce tu email: ")

arroba=email_test.index("@")
usuario=email_test[:arroba]
dominio=email_test[arroba:]
print("Correo: "+email_test)
print("Usuario: "+usuario)
print("Dominio: "+dominio)