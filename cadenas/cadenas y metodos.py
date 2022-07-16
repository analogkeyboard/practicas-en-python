cadena="frase de prueba"
print(cadena.count('pru'))
print(cadena.count('r',0))
print(cadena.lower())
print(cadena.upper())

print(cadena.replace('a','i'))
print(cadena.replace('e','u',2))

cad2='mi cadena es larga'

print(cad2.split('a'))

cad3='Hola Mundo'
print(cad3.split('o',1))

cad4="quiero la palabra hola"
print(cad4.find('a',10,16))

#el join une una cadena de caracteres con un separador
#por ejemplo
cad5='h','o','l','a'
separador=""

print(type(separador.join(cad5)))
print(separador.join(cad5))