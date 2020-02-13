# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 10:06:23 2020

@author: palar
"""

#rango = list( range(10) )
#print(rango)
def validar(name):
    if len(name)<6:
        print('El nombre de usuario debe contener al menos 6 caracteres')
    elif len(name)>12:
        print('El nombre de usuario no puede contener más de 12 caracteres')
    elif name.isalnum()!=True:
        print('El nombre de usuario puede contener solo letras y números')
    else:
        return True

name = input('Ingresa nombre de usuario: ')
vname=validar(name)
print(vname)
#print("Longitud: ",len(name))
#print("Rango: ", list(range(len(name))))
