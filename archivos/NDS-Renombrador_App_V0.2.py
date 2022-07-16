### NDS nombres App
import os
#### fromatos de archivos
formato_juego = (".nds")
formato_imagen = (".png")
#### para encerra la region del juego entre () bien
a = (" (")
b = (")")
c = (" (GameCode - ")
####
region_juego = ("")
codigo_juego = ("")
uno = ("1")
dos = ("2")
tres = ("3")
#### Nik_Roms
nombre_original_juego = ("game.nds")
nuevo_nombre_juego = ("")

#### IG DATOS_EXTRAS_JUEGO
etiqueta_original_icono = ("icono.png")
etiqueta_icono = (" (Icono)")
etiqueta_original_gi = ("info.png")
etiqueta_gi = (" (GameInfo)")
etiqueta_original_mig = ("menu.png")
etiqueta_mig = (" (MenuIniGame)")
etiqueta_original_ig = ("ig.png")
etiqueta_ig = (" (InGame)")

#### IMAGENES_DE_PORTADAS
etiqueta_original_fc = ("frontal.png")
etiqueta_fc = (" (Front-Cover)")
etiqueta_original_bc = ("trasero.png")
etiqueta_bc = (" (Back-Cover)")
etiqueta_original_full = ("full.png")
etiqueta_full = (" (Full-Cover)")

#### IMAGEN_DE_Trajeta
etiqueta_original_gcf = ("tarjeta.png")
etiqueta_gcf = (" (GameCard-Full)")

#### IMAGEN_DE_ETIQUETA/LABELE/STICERK
etiqueta_original_gcl = ("etiqueta.png")
etiqueta_gcl = (" (GameCard-Labele)")

####-----------------------------------------------------
nuevo_nombre_juego=input ("Nombre del juego?: ")
region_juego=input ("Elige el numero de la region del juego - 1:EUR - 2:USA - 3:JAP: ")
codigo_juego=input ("Cual es el codigo de la tarjeta?: ")
#--------------------------------------------------------------------------------------
#MODIFICA KA REGION POR LA DLE NUMERO DE LA VARIABLE AL TEXTO CORESTO
try:
    if region_juego == uno:
        region_juego = ("EUR")
    elif region_juego == dos:
        region_juego = ("USA")
    elif region_juego == tres:
        region_juego = ("JAP")
    #else:
    #    print ("NO es valida la tecla")

    ####-------------------------------------Nik_Roms-------------------------------------
    ### Nombre de rom
    if nombre_original_juego == nombre_original_juego:
        os.rename(nombre_original_juego, nuevo_nombre_juego + a + region_juego + b + c + codigo_juego + b + formato_juego)

    ####--------------------------------DATOS_EXTRAS_JUEGO--------------------------------
    if etiqueta_original_icono == etiqueta_original_icono:
        os.rename(etiqueta_original_icono, nuevo_nombre_juego + a + region_juego + b +   etiqueta_icono   + c + codigo_juego + b + formato_imagen)

    if etiqueta_original_gi == etiqueta_original_gi:
        os.rename(etiqueta_original_gi, nuevo_nombre_juego + a + region_juego + b +   etiqueta_gi   + c + codigo_juego + b + formato_imagen)

    if etiqueta_original_mig == etiqueta_original_mig:
        os.rename(etiqueta_original_mig, nuevo_nombre_juego + a + region_juego + b +   etiqueta_mig   + c + codigo_juego + b + formato_imagen)

    if etiqueta_original_ig == etiqueta_original_ig:
        os.rename(etiqueta_original_ig, nuevo_nombre_juego + a + region_juego + b +   etiqueta_ig   + c + codigo_juego + b + formato_imagen)

    ####-------------------------------IMAGENES_DE_PORTADAS-------------------------------
    if etiqueta_original_fc == etiqueta_original_fc:
        os.rename(etiqueta_original_fc, nuevo_nombre_juego + a + region_juego + b +   etiqueta_fc   + c + codigo_juego + b + formato_imagen)

    if etiqueta_original_bc == etiqueta_original_bc:
        os.rename(etiqueta_original_bc, nuevo_nombre_juego + a + region_juego + b +   etiqueta_bc   + c + codigo_juego + b + formato_imagen)

    if etiqueta_original_full == etiqueta_original_full:
        os.rename(etiqueta_original_full, nuevo_nombre_juego + a + region_juego + b +   etiqueta_full   + c + codigo_juego + b + formato_imagen)

    ####--------------------------------IMAGEN_DE_Trajeta---------------------------------
    if etiqueta_original_gcf == etiqueta_original_gcf:
        os.rename(etiqueta_original_gcf, nuevo_nombre_juego + a + region_juego + b +   etiqueta_gcf   + c + codigo_juego + b + formato_imagen)

    ####-------------------------IMAGEN_DE_ETIQUETA/LABELE/STICERK------------------------
    if etiqueta_original_gcl == etiqueta_original_gcl:
        os.rename(etiqueta_original_gcl, nuevo_nombre_juego + a + region_juego + b +   etiqueta_gcl   + c + codigo_juego + b + formato_imagen)
    ####---FIN---
except FileNotFoundError:
    print("El archivo no fue encontrado")