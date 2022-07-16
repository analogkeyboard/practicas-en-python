class Usuario:
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido

    def saludo(self):
        print("hola,mi nombre es: ",self.nombre,self.apellido)

usuario1=Usuario("carlos","henan")
usuario2=Usuario("andrea","henan")

print(usuario1.nombre,usuario1.apellido)
print(usuario2.nombre,usuario2.apellido)

usuario1.saludo()
usuario1.nombre="chanchito"
#del usuario1.nombre

class Admin(Usuario):
    def superSaludo(self):
        print("Hola, me llamo",self.nombre," y soy administrador")

admin = Admin("tania","hilian")

admin.superSaludo()
admin.saludo()

#usuario.superSaludo()



    


