def numeros(num):
  if num!=51:
    print(num,end=",")
    num+=1
    numeros(num)
  else:
    return

numeros(1)