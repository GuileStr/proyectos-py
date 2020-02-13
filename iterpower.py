# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 11:35:43 2020

@author: palar
"""

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    res=1
    for i in range(1,exp+1):
        res*=base
        #print(res)
    return res
print(iterPower(3,2))