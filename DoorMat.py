# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 09:03:21 2020

@author: palar
"""

n = int(input('Ingresa n: '))
m=n*3
pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))
