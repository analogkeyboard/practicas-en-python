"""class Producto:
    def __init__(self,referencia,tipo,nombre,pvp,desc,productor=None,distribuidor=None,isbn=None,autor=None):
    
        self.referencia=referencia
        self.tipo=tipo
        self.nombre=nombre
        self.pvp=pvp
        self.desc=desc
        self.productor=productor
        self.distribuidor=distribuidor
        self.isbn=isbn
        self.autor=autor
    
adorno=Producto("000A","adorno","vaso adornado",15,"vaso de porcelana con dibujos")

print(adorno.tipo)"""

class Producto(object):
    def __init__(self,referencia,nombre,pvp,descripcion):
        self.referencia=referencia
        self.nombre=nombre
        self.pvp=pvp
        self.descripcion=descripcion

    def __str__(self):
        return """\
REFERENCIA\t{}
NOMBRE\t\t{}
PVP\t\t{}
DESCRIPCION\t{}""".format(self.referencia,self.nombre,self.pvp,self.descripcion)
   
class Adorno(Producto):
    """
    docstring
    """
    pass

adorno =Adorno(1,"vaso adornado",15,"vaso adornado de  porcelana")
#print(adorno)

class Alimento(Producto):
    """
    docstring
    """
    productor=""
    distribuidor=""

    def __str__(self):
        return """\
REFERENCIA\t{}
NOMBRE\t\t{}
PVP\t\t{}
DESCRIPCION\t{}
PRODUCTOR\t{}
DISTRIBUIDOR\t{}""".format(self.referencia,self.nombre,self.pvp,self.descripcion,self.productor,self.distribuidor)

alimento = Alimento(1,"fruta",5,"platano")
alimento.productor="la la"
alimento.distribuidor="le le"
#print(alimento)

class Libro(Producto): 
    isbn=""
    autor=""
    def __str__(self):
        return """\
REFERENCIA\t{}
NOMBRE\t\t{}
PVP\t\t{}
DESCRIPCION\t{}
ISBN\t\t{}
AUTOR\t\t{}""".format(self.referencia,self.nombre,self.pvp,self.descripcion,self.isbn,self.autor)

libro = Libro(20,"libro de cocina",9,"recetas")
libro.isbn="12345"
libro.autor="juan"
#print(libro)

productos = [adorno,alimento,libro]
#productos.append("11")
#print(adorno,alimento,productos)
print()
#for para recorrer los elementos de la lista

"""for p in productos:
    #print(p.referencia,p.nombre,p.autor,"\n")

    if (isinstance(p,Adorno)):
        print("Referencia\tPropiedad")
        print(p.referencia,"\t\t",p.nombre)
    elif isinstance(p,Alimento):
        print(p.referencia,"\t\t",p.referencia)
    elif isinstance(p,Libro):
        print(p.referencia,"\t\t",p.autor)
"""    

def rebaja_pvp(p,rebaja):
    p.pvp=p.pvp-(p.pvp/100*rebaja)
    return p

alimento_rebaja=rebaja_pvp(alimento,10)
print("alimento rebajado: ",alimento_rebaja)