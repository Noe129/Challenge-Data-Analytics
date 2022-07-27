# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 22:54:48 2022

@author: noesi
"""

import os
import Archivos as arch
import pandas as pd

def CapitalizaDicTab(tablas):
    for i in tablas.keys():
        columna = []
        for j in tablas[i]:
            columna.append(j.capitalize())
        tablas[i].columns = columna
    return tablas

def DicTablas(NombreArch, Capitaliza = False):    
    rutas = arch.Leer_Archivos(NombreArch)
    rutas = rutas.split("\n")[:-1]
    datos = {}
    for i in rutas:
        datos[i[:i.index("\\")]] = pd.read_csv(i)
    if Capitaliza:
        CapitalizaDicTab(datos)
    return datos

def TablaUnica(Tablas, NombreArch = None, Lista = None, diccionario = False):
    if NombreArch!= None:
        EncabezadosDeLosDatos = arch.Leer_Archivos(NombreArch).split("\n")
    else:
        EncabezadosDeLosDatos = []
    if Lista != None:
        EncabezadosDeLosDatos = EncabezadosDeLosDatos + Lista
    if(diccionario == True):
        indice = list(Tablas.keys())
    else:
        indice = range(len(Tablas))
    for i in indice:
        for j in Tablas[i].columns:
            if j not in EncabezadosDeLosDatos:
                Tablas[i] = Tablas[i].drop([j], axis=1)
    tabla_unica = Tablas[indice[0]]
    for i in indice[1:]:
        tabla_unica = pd.concat([tabla_unica, Tablas[i]], axis=0)
    return tabla_unica

datos = DicTablas("UltimosArchivos.txt", Capitaliza = True, )
tabla1 = TablaUnica(datos, NombreArch = "Tablas.txt", diccionario = True)
datos = DicTablas("UltimosArchivos.txt", Capitaliza = True)
tabla2 = TablaUnica(datos, Lista = ["Categoria","Fuente", "Provincia"], diccionario = True)
categoria = pd.DataFrame(tabla2["Categoria"].value_counts().reset_index())
categoria.columns = ['Categoria', 'Conteo Categoria']

fuente = pd.DataFrame(tabla2["Fuente"].value_counts().reset_index())
fuente.columns = ['Fuente', 'Conteo Fuente']

provincia = pd.DataFrame(tabla2[["Categoria","Provincia"]].value_counts().reset_index())
provincia.columns = ['Categoria', 'Provincia', 'Conteo Categoriaxprovincia']

df2 = pd.merge(tabla2, categoria, on='Categoria')
df2 = pd.merge(df2, fuente, on='Fuente')
df2 = pd.merge(df2, provincia, on=['Categoria', 'Provincia'])


datos = DicTablas("UltimosArchivos.txt", Capitaliza = True)
cine = ["Cod_loc",
        "Nombre",
        "Provincia",
        "Pantallas",
        "Butacas",
        "Espacio_incaa"]
tabla3 = TablaUnica([datos["salas_de_cine"]], Lista = cine)