query = "hola como hola estas estas hoy?"
my_txt=query.split(" ")
counting_words={}
cont=0

for i in range(0,len(my_txt)):
  firstword=my_txt[i]
  print("first loop:",firstword)
  for j in range(0,len(my_txt)):
   sec_word=my_txt[j]
   #print("\tsecond loop:",sec_word)
   if firstword==sec_word:
     cont+=1
  counting_words[firstword]=cont
  cont=0
print(counting_words)
    