import re

s="10:bd:7a:d6:5c:3e"
p=r"^[0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}$"

regex=re.search(p, s)

if regex:

	print(regex)
	print("valido")
else:
	print("invalido")
