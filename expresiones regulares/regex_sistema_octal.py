import re

s="o7770066"
p=r"^[oO]?[0-7]+$"

regex=re.search(p, s)

if regex:

	print(regex)
	print("valido")
else:
	print("invalido")
