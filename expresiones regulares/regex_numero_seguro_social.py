import re

# pattern=r"^[0-9]]{2}-[0-9]]{2}-[0-9]]{2}-[0-9]]{4}-\d$"
# pattern=r"^\d{2}-\d{2}-\d{2}-\d{4}-\d$"
pattern=r"^(\d{2}-){3}\d{4}-\d$"

string="10-80-60-2265-3"

regex=re.search(pattern, string)

if regex:
	print(regex)
	print("valido")
else:
	print("invalido")