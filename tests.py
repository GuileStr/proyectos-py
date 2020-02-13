# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 11:22:19 2020

@author: palar
"""

#txt = 'ricardo@hotmail.com'
txt = input('Ingresa un correo electronico "Ex: ricardo@gmail.com": ')

x = txt.split('@')
print("Tipo de email: ",x[1])
