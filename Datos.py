# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 21:25:44 2022

@author: noesi
"""

import requests as req
import os
from datetime import datetime
import time



#Función que recibe un nombre y busca ese archivo en la misma carpeta
#Que este codigo, si se da una dirección, se usa en lugar de la del archivo
#En caso de dar la direccion se debe dar el nombre. Siempre dar el nombre con
#La extensión
def Leer_Enlaces(Nombre, direccion = 0):
    contenido = None
    if(direccion == 0):
        local_dir = os.path.dirname(__file__)
        direccion = os.path.join(local_dir, Nombre)
        direccion = direccion.replace("\\", "/")
    try:
        f = open(direccion, "r")
        contenido = f.read()
        f.close()
    except:
        print("Nombre o direccion erronea")
    return contenido

def buscar_enlace(codigo):
    inicio = 0
    fin = codigo.index(".csv")
    while(inicio<fin):
        inicio2 = inicio
        inicio = codigo.index("href", inicio+1)
    enlace = codigo[inicio2+6:fin+4]
    return enlace

def Descarga_datos_gob_arg(Enlace):
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
    enlace = buscar_enlace(codigo)
    archivo = req.get(enlace, allow_redirects=True)
    n = 0
    while(n < len(busqueda)):
        if(enlace.count(busqueda[n]) == 1):
            nombre = resultado[n] + "\\"
            categoria = resultado[n]
        n += 1
    inicio = codigo.index("cambio")
    inicio = codigo.index("de", inicio)
    inicio2 = codigo.index("\\n", inicio+1)
    fecha = codigo[inicio+3: inicio2]
    fecha = fecha.split(" ")
    nombre = nombre + fecha[2] + "-" + fecha[0] + "\\"
    segundos = time.time()
    date = str(datetime.fromtimestamp(segundos))
    date = date[:date.index(" ")]
    date = date.split("-")
    nombre = nombre + categoria + "-" + date[2] + "-" + date[1] + "-" + date[0]
    open(nombre, 'wb').write(archivo.content)
    
    

enlaces = Leer_Enlaces("Enlaces.txt")
if enlaces != None:
    enlaces = enlaces.split("\n")
    for i in enlaces:
        Descarga_datos_gob_arg(i)
