import re
# patron1=r"\d{3}"
# patron2=r"\D{3}"
# patron3=r"\d{3}[a-z]+"
patron4=r"\d+[a-z]+"
texto="345abcd178ghx678"

regex=re.findall(patron4,texto)
print(regex)