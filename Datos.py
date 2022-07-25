# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 21:25:44 2022

@author: noesi
"""

import requests as req
import os
from datetime import datetime
import time
import Archivos as arch

def Descarga_datos_gob_arg(Enlace):
    print(Enlace)
    busqueda = [
        "museo",
        "cine",
        "biblioteca"
        ]
    resultado = [
        "museos",
        "salas_de_cine",
        "bibliotecas_populares",
        ]
    pagina = req.get(Enlace, allow_redirects=True)
    codigo = str(pagina.content)
    enlace = arch.Buscar_Enlace(codigo)
    archivo = req.get(enlace, allow_redirects=True)
    n = 0
    while(n < len(busqueda)):
        if(enlace.count(busqueda[n]) == 1):
            try:
                os.mkdir(resultado[n])
            except OSError:
                print("Ya existe el directorio: " + resultado[n] )
            nombre = resultado[n] + "\\"
            categoria = resultado[n]
        n += 1
    inicio = codigo.index("cambio")
    inicio = codigo.index("de", inicio)
    inicio2 = codigo.index("\\n", inicio+1)
    fecha = codigo[inicio+3: inicio2]
    fecha = fecha.split(" ")
    nombre = nombre + fecha[2] + "-" + fecha[0] 
    try:
        os.mkdir(nombre)
    except OSError:
        print("Ya existe el directorio: " + nombre)
    nombre = nombre + "\\"
    segundos = time.time()
    date = str(datetime.fromtimestamp(segundos))
    date = date[:date.index(" ")]
    date = date.split("-")
    nombre = nombre + categoria + "-" + date[2] + "-" + date[1] + "-" + date[0] + ".csv"
    contenido = str(archivo.content)[2:-1]
    contenido = arch.Conversion(contenido)
    contenido = arch.Normaliza(contenido)
    contenido = contenido.split("\\n")
    arch.Sobrescribir(nombre, contenido)
    return nombre
    
    
nombres = []
enlaces = arch.Leer_Archivos("Enlaces.txt")
if enlaces != None:
    enlaces = enlaces.split("\n")
    for i in enlaces:
        if(len(i)>0):
            nombres.append(Descarga_datos_gob_arg(i))
f = open("UltimosArchivos.txt", "w")
for i in nombres:
    f.write(i+"\n")
f.close()