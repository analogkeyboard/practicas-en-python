class Carta:
    def __init__(self):
        self.palo = "diamantes"
        self.numero = 8

    def mensaje(self):
        print(self.palo,",",self.numero)

carta1= Carta()
carta1.mensaje()