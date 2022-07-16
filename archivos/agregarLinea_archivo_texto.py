#escribir una funcion que reciba nombre y apellido y los vaya agregando a un archivo

def agregNombre(nombre,apellido):
    """
    docstring
    """
    c= open("nombre.txt","a")
    c.write(nombre+" "+apellido+"\n")
    c.close()


agregNombre("chanchito","feliz")
    