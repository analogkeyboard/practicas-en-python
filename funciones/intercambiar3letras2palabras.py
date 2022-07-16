def intercambiar3Letras(palabra1,palabra2):
  print("palabra 1: "+palabra1)
  print("palabra 1: "+palabra2)
  palabra_combinada1=palabra1[:3]+palabra2[3:]
  palabra_combinada2=palabra2[:3]+palabra1[3:]
  return palabra_combinada1+"\n"+palabra_combinada2

print(intercambiar3Letras("tokyo","london"))

