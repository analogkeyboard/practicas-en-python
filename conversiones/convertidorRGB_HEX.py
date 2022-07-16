#convertidor rgb a hexadecimal

red=int(input("Ingresa el color rojo:"))
green=int(input("Ingresa el color verde:"))
blue=int(input("Ingresa el color azul:"))

hex_color = '{:02x}{:02x}{:02x}'.format(red,green,blue)

print("valor hexadecimal: #"+str(hex_color))