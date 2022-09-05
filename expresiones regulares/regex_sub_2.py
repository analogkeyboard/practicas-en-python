import re
cadena="abc@efg"
patron=r"(\w+)@(\w+)"
substitucion=r"\1@123"
regex=re.sub(patron,substitucion, cadena)
print(cadena)
print(regex)