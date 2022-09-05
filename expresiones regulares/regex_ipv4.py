import re

# pattern=r"^([012][0-9][0-9]|25[0-5])$"
#255.255.255.255
pattern=r"^(\d|[01]?\d\d|2[0-4]\d|25[0-5]\.){3}(\d|[01]?\d\d|2[0-4]\d|25[0-5])$"
string="255.255.255.255"
# string="AIOZ 111a A@=& ;!#*"
regex=re.search(pattern, string)
if regex:
	print(regex)
	print("valido")
else:
	print("invalido")

	