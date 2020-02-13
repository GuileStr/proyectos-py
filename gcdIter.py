# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 12:41:26 2020

@author: palar
"""

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    value=0
    if a<b:
        value=a
        while a>0:
            if b%a==0 and value%a==0:
                return a
            a-=1
    else:
        value=b
        while b>0:
            if a%b==0 and value%b==0:
                return b
            b-=1
    
print(gcdIter(9,12))