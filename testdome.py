# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 16:02:47 2020

@author: palar
"""

l = [1,2,'a',3,'b']
print(l)
for i in range(len(l)):
    #print(l[i])
    if l[i].isalpha:
        l.remove(i)
        
print(l)