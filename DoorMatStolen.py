# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 09:14:50 2020

@author: palar
"""

n, m = map(int,input().split()) #1
pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]#2
print('\n'.join(pattern + ['Erika bb uwu'.center(m, '-')] + pattern[::-1]))#3

#1:
# map= Agarramos toda la linea de comando que sea ingresada
# Hacemos el int, input para convertirlo como entero y pues agarrar los datos
# y hacemos el split para convertirlos en mas de un valor si existe 
# un separador en este caso un espacio en blanco

#2:
# Creamos un patron para escribir el mensaje de bienvenida
#Todo dentro del ciclo  for i in range(n//2)
#       ('.|.'*(2*i + 1))
#   Esta primer parte genera los puntos medios justo al centro y guarda su pos.
#       .center(m, '-')
#   Esto agrega guiones medios para llenar los campos hasta la fig anterior

#3:
#Aquí imprimimos con '\n'.join()
#Imprimimos nuestro pattern#Este pattern es, agregar lo del centro y otro más a su izquierda '.|.'
# y sumamos la palabra Welcome en el centro
#De la siguiente manera + ['WELCOME'.center(m, '-')] +
#Despues añadimos otro pattern para cerrar con otro '.|.' y sus respectivos guines
#En lugar del mensaje welcome ponemos '::-1' que lo hace "negativo"
#En este caso ser negativo es el mismo patron invertido