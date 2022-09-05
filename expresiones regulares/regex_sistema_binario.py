import re

s="b0010011101001"
p=r"^[bB]?[0-1]+$"

regex=re.search(p, s)

if regex:

	print(regex)
	print("valido")
else:
	print("invalido")
