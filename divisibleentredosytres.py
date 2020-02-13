# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 12:17:07 2020

@author: palar
"""
x = int (input('Ingresa un integer: '))
if x%2 ==0:
    
    if x%3==0:
        print('')
        print('Divisible entre 2 y3 ')
    else:
        print('')
        print('Divisible entre 2 y 3 no')
elif x%3==0:
    print('')
    print('Divisible entre 3 y 2 no')
print('Fin')