#escribir una funcion que indique si el usuario es mayor de edad

def esmayor(usuario):
    return usuario.edad > 18

class Usuario(object):
    """
    docstring
    """
    def __init__(self,edad):
        self.edad=edad

usuario1 = Usuario(15)
usuario2 = Usuario(21)

print(esmayor(usuario1))
print(esmayor(usuario2))
