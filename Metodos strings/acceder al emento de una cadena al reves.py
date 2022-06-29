#para acceder al ultimo elemento el signo de menos (-)
#y la ultima posicion + 1, por ejemplo, la palabra 'casa' tiene
#4 elementos desde el 0 al 3 , entonces para ir en 'reversa'
#decimos que -1 es el ultimo elemento , luego el antepenultimo seria -2 y asi
#sucesivamente veamoslo de forma grafica , si queremos que sea normal es:
#C=0
#A=1
#S=2
#A=3

#entonces para ir de forma inversa seria:
#A=-1
#S=-2
#A=-3
#C-4

palabra="casa"

#esta es la forma manual de imprimir cada elemento de la palabra
print palabra[-1] #nos da el ultimo elemento
print palabra[-2]
print palabra[-3]
print palabra[-4] #nos da el primer elemento
