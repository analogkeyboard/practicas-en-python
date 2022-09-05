import random
import pandas as pd

random.seed(1)

xi=[random.uniform(-100,100) for i in range(10)]
yi=[random.uniform(-100,100) for i in range(10)]

print("Individuo","\t","xi","\t","yi")
i=0
for x in range(1):
	for y in range(10):
		print(i,"\t","{:.2f}".format(xi[i]),"\t\t","{:.2f}".format(yi[i]))
		i=i+1
	print()