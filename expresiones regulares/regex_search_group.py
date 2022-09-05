import re

regex1=r"ol"
cadena1="hologrolama"

print("Expresion Regular:",regex1)
print("Cadena:",cadena1)
a=re.search(regex1, cadena1).group()
print("Expresion regular encontrad:",a)
print()

regex2=r"\d\d\d"
cadena2="986hola"

print("Expresion Regular:",regex2)
print("Cadena:",cadena2)
b=re.search(regex2,cadena2 ).group()
print("Expresion regular encontrad:",b)
print()
regex3=r"\d\d\d"
cadena3="adios123"

print("Expresion Regular:",regex3)
print("Cadena:",cadena3)
c=re.search(regex3,cadena3 ).group()
print("Expresion regular encontrad:",c)
