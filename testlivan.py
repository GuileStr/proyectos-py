# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 09:43:47 2020

@author: palar
"""

greeting = 'Hello!'
count = 0

for letter in greeting:
    count += 1
    if count % 2 == 0:
        print(letter)
    print(letter)

print('done')