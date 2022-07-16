class Galleta():
    chocolate=False
    def __init__(self,sabor=None,color=None):
        self.sabor=sabor
        self.color=color

        if sabor is not None and color is not None:
            print("Galleta creada: ",sabor,",",color)

            
    def chocolatear(self):
        """
        docstring
        """
        self.chocolate=True

    def tiene_chocolate(self):
        if self.chocolate:
            print("soy una galleta con chocolate")
        else:
            print("soy una galleta sin  chocolate")

galleta1= Galleta("dulce","marron")
galleta2= Galleta("dulce","gris")

#galleta1.sabor="salado"
#galleta1.color="marron"
#print(type(galleta1))
"""print("sabor de la galleta: ",galleta1.sabor)
print("color de la galleta: ",galleta1.color)
print("Tiene chocolate?: ",galleta1.chocolate)
galleta1.tiene_chocolate()
print("Tiene chocolate?: ",galleta1.chocolate)
galleta1.chocolatear()
galleta1.tiene_chocolate()"""
