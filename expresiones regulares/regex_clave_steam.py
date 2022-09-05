import re
#formato de clave de steam

#AAAAA-BBBBB-CCCCC
#AAAAA-BBBBB-CCCCC-DDDDD-EEEEE
#237ABCDGHJLPRST 23

pattern=r"^([A-Z0-9]{5}-?){3}([A-Z0-9]{5}-[A-Z0-9]{5})?$|^237[A-DGHJLPR-T]{12}\s23$"

string1="64JH5-JHB78-9H8JM"
string2="64JH5-JHB78-9H8JM-AAAAA-BBBBB"
string3="237DJCCDLADDHAJ 23"

regex1=re.search(pattern, string1)
regex2=re.search(pattern, string2)
regex3=re.search(pattern, string3)

if regex1 and regex2 and regex3:
	print(regex1)
	print(regex2)
	print(regex3)
	print("valido")
else:
	print("invalido")