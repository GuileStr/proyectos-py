# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 10:02:56 2020

@author: palar
"""

def contarElementosLista(lista):
    return {i:lista.count(i) for i in lista} 
    #El for en una sola linea se pone primero la accion y después el forxd
    # En este caso:
    #Agarro "i:" como llave
    #Y "lista.count(i)" como las veces que se repite el numero dentro de la lista
    #Asíes. Arriba yo, mi apá y la chona

arr = list(map(int, input('Pasa el array plocs: ').split()))
jeje = contarElementosLista(arr)
#print(jeje)
for i in jeje:
    #print("Llave: ",i, "y value: ",jeje.get(i))
    if i == jeje.get(i):
        print(i)