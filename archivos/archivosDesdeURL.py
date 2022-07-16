from urllib import request
# f = request.urlopen('https://raw.githubusercontent.com/analogkeyboard/ficheros-de-texto-de-practica-python/main/fichero.txt')
f = request.urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt')
datos = f.read()
print(datos.decode('utf-8'))
