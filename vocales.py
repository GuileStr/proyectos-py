# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 15:59:56 2020

@author: palar
"""

s = 'aeiouasdxñzlxmcoaskd'
con=0
for char in s:
    if char == 'a' or char=='e' or char=='i' \
    or char=='o' or char=='u':
        con+=1
print(con)
        