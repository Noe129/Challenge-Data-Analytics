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
    if(direccion == 0):
        local_dir = os.path.dirname(__file__)
        direccion = os.path.join(local_dir, Nombre)
        direccion = direccion.replace("\\", "/")
    f = open(direccion, "r")
    contenido = f.read()
    f.close()
    return contenido

enlaces = Leer_Enlaces("Enlaces.txt")
enlaces = enlaces.split("\n")
file = req.get(enlaces[0], allow_redirects=True)

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

s = str(file.content)
inicio = 0
fin = s.index(".csv")
while(inicio<fin):
    inicio2 = inicio
    inicio = s.index("href", inicio+1)
file = req.get(s[inicio2+6:fin+4], allow_redirects=True)
n = 0
while(n < len(busqueda)):
    if(s[inicio2+6:fin+4].count(busqueda[n]) == 1):
        nombre = resultado[n] + "\\"
        categoria = resultado[n]
    n += 1
inicio = s.index("cambio")
inicio = s.index("de", inicio)
inicio2 = s.index("\\n", inicio+1)
fecha = s[inicio+3: inicio2]
fecha = fecha.split(" ")
nombre = nombre + fecha[2] + "-" + fecha[0] + "\\"

segundos = time.time()
date = str(datetime.fromtimestamp(segundos))
date = date[:date.index(" ")]
date = date.split("-")
nombre = nombre + categoria + "-" + date[2] + "-" + date[1] + "-" + date[0]

open('aaaa.csv', 'wb').write(file.content)