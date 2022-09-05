import re
rgx=r"Python$"
c="Python no sólo es un lenguaje de programación, Python es mi lenguaje de programacón favorito.Python"
m=re.search(rgx, c)
print(m)
