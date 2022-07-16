palabra=input("palabra: ")

if palabra.lower()==palabra[::-1].lower():
  print(palabra+" == "+palabra[::-1])
  print(palabra+" es palindromo o capicua")
else:
  print(palabra+" != "+palabra[::-1])
  print(palabra+" no es palindromo o capicua")
  