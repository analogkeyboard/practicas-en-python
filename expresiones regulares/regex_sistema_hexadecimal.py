import re

s="#AAA"
p=r"^#\b[a-fA-F0-9]{3}\b|[a-fA-F0-9]{6}$"

regex=re.search(p, s)

if regex:

	print(regex)
	print("valido")
else:
	print("invalido")
