#diccionarios
diccionario={
"gato":"karen",
"raza":"persa",
"edad":5
}

diccionario2={}
print("diccionario:"+str(diccionario))
"""
print(diccionario["raza"])
print(diccionario.get("edad"))
print(diccionario.keys())
print(diccionario.values())
print(diccionario.items())
diccionario2=diccionario.copy()
print("copia diccionario:",diccionario2)

diccionario["ronronea"] = "si"
print(diccionario)
diccionario.clear()
print(diccionario)
"""

gatitos={
    "fluffy":{
        "nombre":"fluffy",
        "edad":4
    },
    "mamba":{
        "nombre":"black mamba",
        "edad":12
    }
}
print("gatitos:",gatitos)

perritos=dict(nombre="chanchito feliz",edad=4)
print("perritos:",perritos)
