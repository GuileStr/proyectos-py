# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 11:44:32 2020

@author: palar
"""
   
    
def recurPower(base, exp):
    if exp==1:
        return base
    elif exp==0:
        return 1
    else:
        print(exp,"veces",3,"=",base)        
        return base*recurPower(base,exp-1)
print(recurPower(9,0))