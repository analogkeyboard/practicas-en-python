import re
#patron = re.compile(r"\d\d\d")
patron = re.compile(r"\d"*3)
a=patron.search("hola402adios").group()
b=patron.search("986hola").group()
c=patron.search("adios123").group()

print("Patron encontrado:",a)
print("Patron encontrado:",b)
print("Patron encontrado:",c)


d=patron.search("adios1x23")
if d is None:
	print("No existe concidencias")
