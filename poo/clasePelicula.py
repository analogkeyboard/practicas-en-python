class Pelicula():
    def __init__(self,tit,dur,lanz):
        self.tit=tit
        self.dur=dur
        self.lanz=lanz
        print("Pelicula creada: ",self.tit)

    #destructor de clase
    def __del__(self):
        print("se esta borrando: ",self.tit)

    def __str__(self):
        #return "titulo:",self.tit,"lanzamiento: ",self.lanz
        return "{} {}".format(self.tit,self.lanz)

    def __len__(self):
        return self.dur
        

p1 = Pelicula("el padrino",175,1972)
#print(str(p1))
#del(p1)
#print(len(p1))

class Catalogo(object):
    peliculas = []
    def __init__(self,peliculas=[]):
        self.peliculas
    
    def agregar(self,p):
        """
        docstring
        """
        self.peliculas.append(p)

    def mostrar(self):
        for p in self.peliculas:
            print("lista:",p)
    
p2=Pelicula("matrix",120,1990)

c= Catalogo([p1])
c.agregar(Pelicula("a",123,1999))
c.mostrar()
c.agregar(Pelicula("b",456,1999))
c.mostrar()

class Ejemplo():
    #atributo privado
    __atributoPrivado="soy un atributo privado"

    def __metodoPrivado(self):
        print("metod privado")

e = Ejemplo()
e.metodoPrivado()