import re
rgx=r"\S[a-zA-Zóúí]+"
c="Cython no es ningún lenguaje de programación y Nython tampoco pero Python sí"
m=re.search(rgx, c)
print(m)

m2=re.findall(rgx, c)
print(m2)

m3=re.sub(r"\s", "\t?\t", c)
print(m3)
