import pandas

#forma 1
data=pandas.read_excel("mi_excel.xlsx")
get_email=data.get("name")
list_email=list(get_email)
for x in list_email:
  print(x)
