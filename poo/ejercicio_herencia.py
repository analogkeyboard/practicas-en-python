class Animal:
    """
    docstring
    """
    def __init__(self,nombre,onomatopeya):
        self.nombre=nombre
        self.onomatopeya=onomatopeya
    
    def saludo(self):
        print("Hola soy un", tipo," y mi sonido es",self.onomatopeya)

class Gato(Animal):
    """
    docstring
    """
    tipo="gato"
    def __init__(self,nombre,onomatopeya):
        Animal.__init__(self,nombre,onomatopeya)
        print("hola, soy un gato extendido")
    
class Perro(Animal):
    """
    docstring
    """
    tipo="perro"
    def __init__(self,nombre,onomatopeya):
        super().__init__(nombre,onomatopeya)
        print("instanciando un perro")

class Canario(Animal):
    """
    docstring
    """
    tipo="canario"
    def __init__(self,saludo):
        print("hola")

gato=Gato("fluffy","maullido")
gato.saludo()

perro=Perro("firulais","ladrido")
perro.saludo()

canario=Canario("canario")
canario.saludo()