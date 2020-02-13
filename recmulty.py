# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 12:04:40 2020

@author: palar
"""

def multi(a,b):
    if b==1:
        return a
    else:
        return a+multi(a,b-1)
    
print(multi(10,10))