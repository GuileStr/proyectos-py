# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 12:22:32 2020

@author: palar
"""
### DICCIONARIOS Y CONSULTAS EN PYTHON ###
dicc={'Wapo':'Ringuin','Escuelas':['Unipoli','utd']}
print(dicc['Wapo'])        ## Consulta en diccionario utilizando la KEY
print(dicc['Escuelas'][0]) ## Consulta a arreglo dentro de diccionario

##  DICCIONARIO EN PYTHON CON CICLO PARA RECORRERLO TODO
dic = {'0':'Ricardo','2':'Reyes',"ke":"kas"}
for k in dic:  ##Ciclar "dic" con una variable "k" que se convierte en la llave. No necesariamente numericas
    print(k," : ",dic[k]) ## k = KEY && dic[k] = Buscar la llave en el diccionario
    
##Abr
diccio=dict(name='Ricardo',apellido='Reyes')
print(diccio['name'])