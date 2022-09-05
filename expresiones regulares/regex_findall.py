import re
patron="Python"
texto="Programa en Python es mi blog favorito de Python, y gracias a él me estoy convirtiendo en todo un Pythonista."

regex=re.findall(patron,texto)
print("Expresion Regular encontrada:",regex)