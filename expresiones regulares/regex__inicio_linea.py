import re
p=r"^\d{0,6}$"
t="444444"
r=re.search(p, t)
print(r)