# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 12:21:43 2020

@author: palar
"""

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if b==0:
        return a
    elif a>b:
        return gcdRecur(b,a%b)
    else:
        return gcdRecur(a,b%a)
#    maxi=max(a,b)
#    if b==0:
#        return a
#    elif maxi==a:
#        return a
#    else:
#        print(b)
#        return b
        
print(gcdRecur(7,12))
