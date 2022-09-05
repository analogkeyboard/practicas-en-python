import re

pattern=r"^(\+[0-9]{2})?\s?\([0-9]{3}\)\s[0-9]{3}-[0-9]{4}$"
string="+12 (345) 678-9012"
# string=" (686) 123-4567"
# string="+52"
regex=re.search(pattern, string)
if regex:
	print(regex)
	print("valido")
else:
	print("invalido")
