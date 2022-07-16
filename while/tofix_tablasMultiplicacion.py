opc=None

tabla=int(input("que tabla quieres?: "))
cantidad=int(input("cantidad?: "))

while opc1:
  for i in range(0,cantidad+1):
     print(tabla,"x",i,"=",tabla*i)
  
  print("desea continuar? 1-si, 2-no")
  
  opc=int(input())
else:
  exit()
  
