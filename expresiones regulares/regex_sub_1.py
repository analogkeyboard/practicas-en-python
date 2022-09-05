import re
patron=r"\d"
cadena="345abcdefg987"
regex=re.sub(patron, "-", cadena)
print(cadena)
print(regex)