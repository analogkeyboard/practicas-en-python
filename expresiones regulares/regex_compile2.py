import re
regex = re.compile(r"(\d+)-[A-Za-z]+")
m=regex.search("23-CDb")
print(m)
print(m.group(0))
print(m.group(1))