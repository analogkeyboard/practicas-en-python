#ejercicio herencia multiple
class A:
    def __init__(self):
        print("soy de clase A")
    def a(self):
        print("este metodo lo heredo de A")

        

class B:
    def __init__(self):
        print("soy de clase B")
    def b(self):
        print("\neste metodo lo heredo de B")

#
class C(B,A):
    #print("soy de clase C")
    def c(self):
        print("\neste metodo es de C")

c=C()
c.a()
c.b()
c.c()