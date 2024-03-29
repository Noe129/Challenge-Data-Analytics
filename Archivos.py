# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 23:14:43 2022

@author: noesi
"""

import os

#Función que recibe un nombre y busca ese archivo en la misma carpeta
#Que este codigo, si se da una dirección, se usa en lugar de la del archivo
#En caso de dar la direccion se debe dar el nombre. Siempre dar el nombre con
#La extensión
def Leer_Archivos(Nombre, direccion = 0):
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

def Buscar_Enlace(codigo):
    inicio = 0
    fin = codigo.index(".csv")
    while(inicio<fin):
        inicio2 = inicio
        inicio = codigo.index("href", inicio+1)
    enlace = codigo[inicio2+6:fin+4]
    return enlace

def Sobrescribir(Nombre, Texto):    
    try:
        f = open(Nombre, "w", encoding="utf-8")
        for i in Texto:
            f.write(i+"\n")
        f.close()
    except:
        print("Direccion erronea")
            
def Conversion(cadena):
    f = open("Conversion.csv", "r", encoding="utf-8")
    contenido = f.read()
    f.close
    contenido = contenido.split("\n")
    for i in range(len(contenido)):
        contenido[i] = contenido[i].split(",")
    for i in range(len(contenido)):
        if(len(contenido[i]) > 2):
            cadena = cadena.replace(contenido[i][2], contenido[i][1])
    return cadena

def Normaliza(cadena):
    remplazar = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
        ("\\r", ""),
        ("Direccion","Domicilio"),
        ("direccion","Domicilio")
        )
    for a, b in remplazar:
        cadena = cadena.replace(a,b)
    return cadena