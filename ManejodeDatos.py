# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 22:54:48 2022

@author: noesi
"""

import os
import Archivos as arch
import pandas as pd

rutas = arch.Leer_Archivos("UltimosArchivos.txt")

rutas = rutas.split("\n")[:-1]
datos = {}
aaaaaaa = pd.read_csv(rutas[0])
# for i in rutas:
#     datos[i[:i.index("\\")]] = pd.read_csv(i)
    

# CarpetasDisponibles = []
# for i in os.listdir():
#     if i in ListaBuscar:
#         CarpetasDisponibles.append(i)
    