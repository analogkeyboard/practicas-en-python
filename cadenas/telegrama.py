cadena=" Llego manana . alrededor . del mediodia .  "

def telegrama(texto):

	cadena_strip=cadena.strip()
	cadena_split=cadena_strip.split()

	print("\ncadena original: "+cadena+"\n")


	for palabra in cadena_split:

		if len(palabra)>5 and palabra!='stopstop':
			palabra=palabra[:5]+'@'
		
		if cadena_split[-1]=='.':
			cadena_split[-1]='stopstop'

		if palabra!=cadena_split[-1] and palabra=='.':
			palabra='stop'
		
		print(palabra+" ",end="")
	
telegrama(cadena)