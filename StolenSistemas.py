# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 09:42:01 2020

@author: palar
"""


st=int(input())

w=len(bin(st)[2:])

for i in range(1,st+1):
    print (str(i).rjust(w,' '),
           str(oct(i)[2:]).rjust(w,' '),
           str(hex(i)[2:].upper()).rjust(w,' '),
           str(bin(i)[2:]).rjust(w,' '),sep=' ')