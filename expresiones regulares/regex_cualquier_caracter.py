import re
rgx=r".ython"
c="Cython no es ningún lenguaje de programación y Nython tampoco pero Python sí"
m=re.search(rgx, c)
print(m)

m2=re.findall(rgx, c)
print(m2)
