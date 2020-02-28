# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 15:52:06 2020

@author: palar
"""
a=[-19,-17,-15,-5,13,18]
b=[-14,-13,-11,1,6,7,14,16,18]

print("a",a)
print("b",b)
c=[]
for i in a:
    if i in a and i in b:
        c.append(i)
print("c",c)