import os

#path="C:\\Users\\T\\Desktop\\practicas_python_2022\\archivos\\"
path=".\\"
with os.scandir(path) as item:
# with os.listdir(path) as item:
    for entrada in item:
        #if no|t entrada.name.startswith('.') and entrada.is_file():
        if  entrada.is_file():
            print(entrada.name)