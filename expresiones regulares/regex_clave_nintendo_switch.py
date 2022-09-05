import re

pattern=r"^([^IOZa-z@=&;!#*]{4}\s){3}[^IOZa-z@=&;!#*]{4}$"
string="ABCD 1111 JKLM NPQR"
# string="AIOZ 111a A@=& ;!#*"
regex=re.search(pattern, string)
if regex:
	print(regex)
	print("valido")
else:
	print("invalido")

	