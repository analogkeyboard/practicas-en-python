# -*- coding: utf-8 -*-
n="sakuray"
largo=len(n)
ultimo= -1
contador=0
contador2=0
print "cadena: ",n
print "elementos: ",largo
print "ultimo elemento: ",ultimo
print "ultima letra: ",n[ultimo]


print
print "ELEMENTO\t\tINDICE\t\t\t-INDICE"
for x in n:
	
	print "elemento =",x,"\t\t","indice[",contador,"] = ",n[contador],"\t\t","indice=[",ultimo,"] = ",n[ultimo]
	ultimo=ultimo-1
	contador=contador+1


