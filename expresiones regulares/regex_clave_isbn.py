import re

pattern=r"^97(8|9)-[0-9]{3}-[0-9]{0,7}-[0-9]{0,6}-[0-9]$"
string="978-980-14-251111-5"
regex=re.search(pattern, string)
if regex:
	print(regex)
else:
	print("no valido")